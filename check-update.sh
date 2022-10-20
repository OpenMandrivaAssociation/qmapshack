#!/bin/sh
curl "https://github.com/Maproom/qmapshack/tags" 2>/dev/null |grep "tag/V_" |sed -e 's,.*tag/V_,,;s,\".*,,;' |head -n1


