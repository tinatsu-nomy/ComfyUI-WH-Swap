# ComfyUI-WH-Swap

A minimal ComfyUI custom node for specifying Width and Height,
swapping them with a button, and outputting both values as `INT`.

## Features

- Width input: `INT`
- Height input: `INT`
- Width output: `INT`
- Height output: `INT`
- `↔ Swap Width / Height` button
- No external Python packages
- No Google API / Gemini dependency
- No network access

## Install

Copy this directory to:

```text
ComfyUI/custom_nodes/ComfyUI-WH-Swap
```

The resulting layout should be:

```text
ComfyUI/
└── custom_nodes/
    └── ComfyUI-WH-Swap/
        ├── __init__.py
        ├── nodes.py
        ├── README.md
        └── web/
            └── wh_swap.js
```

Restart ComfyUI after installation.

## Node

Search for:

```text
Width / Height Swap
```

Category:

```text
utils/size
```

Default values:

- width: 1024
- height: 1024

Example:

```text
width  = 1344
height = 768

↓ press Swap

width  = 768
height = 1344
```

Both outputs are standard ComfyUI `INT` values.
