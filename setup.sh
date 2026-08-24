mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"\"\n\
passwordRequired = false\n\
enableCORS = false\n\
\n\
[server]\n\
headless = true\n\
enableXsrfProtection = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
