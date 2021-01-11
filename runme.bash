sass \
    built/reveal.js/css/theme/source/droub.scss \
    built/reveal.js/css/theme/droub.css \
    -I built/reveal.js/css \
    --no-source-map

#asciidoctor-revealjs source/part1.adoc -D built -a answers
asciidoctor-revealjs source/part1.adoc -D built -a answers2 -a answers
