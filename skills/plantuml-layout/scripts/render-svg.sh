#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Uso:
  render-svg.sh <archivo.puml> [directorio_salida]

Comportamiento:
  - Si se indica un directorio de salida, renderiza ahi.
  - Si no se indica y la ruta contiene /src/, usa el directorio espejo en /out/.
  - Si no se puede inferir /out/, renderiza en el mismo directorio del .puml.
EOF
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

source_file="$1"

if [[ ! -f "$source_file" ]]; then
  echo "No existe el archivo: $source_file" >&2
  exit 1
fi

abs_source="$(python3 -c 'import os,sys; print(os.path.abspath(sys.argv[1]))' "$source_file")"
source_dir="$(dirname "$abs_source")"
source_name="$(basename "$abs_source")"

if [[ $# -eq 2 ]]; then
  output_dir="$2"
else
  if [[ "$source_dir" == *"/src/"* ]]; then
    output_dir="${source_dir/\/src\//\/out\/}"
  else
    output_dir="$source_dir"
  fi
fi

abs_output="$(python3 -c 'import os,sys; print(os.path.abspath(sys.argv[1]))' "$output_dir")"
mkdir -p "$abs_output"

relative_output="$(python3 -c 'import os,sys; print(os.path.relpath(sys.argv[2], sys.argv[1]))' "$source_dir" "$abs_output")"

(
  cd "$source_dir"
  plantuml -tsvg -o "$relative_output" "$source_name"
)

echo "SVG generado en: $abs_output"
