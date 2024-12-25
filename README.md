## testing

```
uv run pytest
```

## mutation testing

```
uv run cosmic-ray init mutation-testing.toml session.sqlite
uv run cosmic-ray exec mutation-testing.toml session.sqlite
uv run cr-html session.sqlite reports/mutationtesting.html 
```