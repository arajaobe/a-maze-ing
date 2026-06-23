#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   parsing.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:23:15 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/22 13:23:16 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


#parsing

def parse_config(filename):
    config = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key] = value
    return config


def get_config_values(cfg):
    width = int(cfg.get("WIDTH", "0"))
    height = int(cfg.get("HEIGHT", "0"))

    entry = tuple(map(int, cfg.get("ENTRY", "0,0").split(",")))
    exit = tuple(map(int, cfg.get("EXIT", f"{width-1},{height-1}").split(",")))

    output_file = cfg.get("OUTPUT_FILE", "maze.txt")

    # Perfect flag
    perfect_str = cfg.get("PERFECT", "false").lower()
    if perfect_str not in ("true", "false"):
        raise ValueError("PERFECT must be 'True' or 'False'.")
    perfect = (perfect_str == "true")

    try:
        validate_config(width, height, entry, exit)
    except Exception as e:
        print(f"{e}")
        exit(1)

    return width, height, entry, exit, output_file, perfect


def validate_config(width, height, entry, exit):
    # Width/height must be positive
    if width <= 0 or height <= 0:
        raise ValueError("WIDTH and HEIGHT must be positive integers.")

    # Entry must be inside bounds
    if not (0 <= entry[0] < width and 0 <= entry[1] < height):
        raise ValueError(f"ENTRY {entry} is outside maze bounds.")

    # Exit must be inside bounds
    if not (0 <= exit[0] < width and 0 <= exit[1] < height):
        raise ValueError(f"EXIT {exit} is outside maze bounds.")

    # Entry and exit must be different
    if entry == exit:
        raise ValueError("ENTRY and EXIT must be different cells.")

    return True
