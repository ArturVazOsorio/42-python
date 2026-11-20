#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_command_quest.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/10/27 18:02:33 by aantela-         #+#    #+#              #
#    Updated: 2026/10/27 18:23:48 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys

if __name__ == "__main__":
    print("=== Comand quest ===")
    prog_name = sys.argv[0]
    print(f"Program name: {prog_name}")
    len_argv = len(sys.argv)
    if len_argv > 1:
        for x in range(len(sys.argv)):
            print(f"Argument {x}: {sys.argv[x]}")
    print(f"Total arguments: {len_argv}")
