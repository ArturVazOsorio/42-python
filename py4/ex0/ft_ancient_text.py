#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/09 20:15:58 by aantela-            #+#    #+#            #
#   Updated: 2026/11/09 20:48:22 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys, typing

def main()-> None:
    
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print(f"Acessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1],"r")
        conteudo: str = file.read()
        file.close()
        print("---\n",conteudo,"\n---")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"{e.__class__.__name__}: {e}")
        return
    print(f"file {sys.argv[1]} closed.")
    
    
if __name__=="__main__":
    main()