#!/usr/bin/env python3
"""Inject draft-kit/players.json into index.html between the data markers.

Usage:
  python3 build.py            # inject players.json into index.html
  python3 build.py --check    # print the dataAsOf stamp currently embedded in index.html
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
HTML = HERE / "index.html"
DATA = HERE / "players.json"
START = "/*__PLAYER_DATA_START__*/"
END = "/*__PLAYER_DATA_END__*/"


def main() -> int:
    html = HTML.read_text(encoding="utf-8")
    start = html.index(START)
    end = html.index(END)
    if "--check" in sys.argv:
        blob = html[start + len(START):end]
        m = re.search(r'"dataAsOf"\s*:\s*"([^"]*)"', blob)
        print(m.group(1) if m else "(no dataAsOf found)")
        return 0
    data = json.loads(DATA.read_text(encoding="utf-8"))
    if "</script" in json.dumps(data):
        print("refusing to inject: data contains '</script'", file=sys.stderr)
        return 1
    blob = "\nwindow.DK_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n"
    HTML.write_text(html[:start + len(START)] + blob + html[end:], encoding="utf-8")
    print(f"injected {DATA.name} ({DATA.stat().st_size} bytes) into {HTML.name}; dataAsOf={data['meta'].get('dataAsOf')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
