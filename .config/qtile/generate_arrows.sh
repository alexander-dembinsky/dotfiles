#!/usr/bin/env bash

generate_right_arrow() {
  color=$1
  outfile=$2
  SVG=`cat << EOF
<svg
   width="60.472649"
   height="120.9453"
   viewBox="0 0 16.000054 32.000109"
   version="1.1"
   id="svg270"
   inkscape:version="1.1 (c4e8f9ed74, 2021-05-24)"
   sodipodi:docname="arrow_left_primary.svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <sodipodi:namedview
     id="namedview272"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0"
     inkscape:document-units="mm"
     showgrid="false"
     inkscape:zoom="5.3664983"
     inkscape:cx="6.2424319"
     inkscape:cy="65.219437"
     inkscape:window-width="1904"
     inkscape:window-height="1152"
     inkscape:window-x="6"
     inkscape:window-y="38"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer1"
     width="16mm"
     units="px"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0" />
  <defs
     id="defs267" />
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-63.058166,-41.824319)">
    <path
       id="rect480"
       style="fill:#${color}ff;stroke-width:0.264583"
       d="M 63.058166,41.824319 V 73.824432 L 79.058221,57.823861 v -0.05685 z" />
  </g>
</svg>
EOF`
  echo "$SVG" > $outfile
}

generate_left_arrow() {
  color=$1
  outfile=$2
  SVG=`cat << EOF
<svg
   width="60.472649"
   height="120.9453"
   viewBox="0 0 16.000054 32.000109"
   version="1.1"
   id="svg270"
   inkscape:version="1.1 (c4e8f9ed74, 2021-05-24)"
   sodipodi:docname="arrow_left_purple.svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <sodipodi:namedview
     id="namedview272"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0"
     inkscape:document-units="mm"
     showgrid="false"
     inkscape:zoom="5.3664983"
     inkscape:cx="-8.6648681"
     inkscape:cy="65.219437"
     inkscape:window-width="1904"
     inkscape:window-height="1152"
     inkscape:window-x="6"
     inkscape:window-y="38"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer1"
     width="16mm"
     units="px"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0" />
  <defs
     id="defs267" />
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-63.058166,-41.824319)">
    <path
       id="rect480"
       style="fill:#${color}ff;stroke-width:0.999999"
       d="m 298.80273,158.07617 v 120.94531 l -60.47265,-60.4746 v -0.21485 z"
       transform="scale(0.26458333)" />
  </g>
</svg>
EOF` 
  echo "$SVG" > $outfile
}

if [ $# -ne 2 ]; then
  echo "Usage: $0 {primary_color_hex} {secondary_color_hex}"
  echo "Example: $0 808080 222222"
fi


generate_left_arrow $1 "$HOME/.config/qtile/img/arrow_left_primary.svg"
generate_left_arrow $2 "$HOME/.config/qtile/img/arrow_left_secondary.svg"

generate_right_arrow $1 "$HOME/.config/qtile/img/arrow_right_primary.svg"
generate_right_arrow $2 "$HOME/.config/qtile/img/arrow_right_secondary.svg"
