0           0 RESUME                   0

  1           2 LOAD_CONST               0 (0)
              4 LOAD_CONST               1 (None)
              6 IMPORT_NAME              0 (os)
              8 STORE_NAME               0 (os)
             10 LOAD_CONST               0 (0)
             12 LOAD_CONST               1 (None)
             14 IMPORT_NAME              1 (sys)
             16 STORE_NAME               1 (sys)
             18 LOAD_CONST               0 (0)
             20 LOAD_CONST               1 (None)
             22 IMPORT_NAME              2 (requests)
             24 STORE_NAME               2 (requests)
             26 LOAD_CONST               0 (0)
             28 LOAD_CONST               1 (None)
             30 IMPORT_NAME              3 (re)
             32 STORE_NAME               3 (re)
             34 LOAD_CONST               0 (0)
             36 LOAD_CONST               1 (None)
             38 IMPORT_NAME              4 (random)
             40 STORE_NAME               4 (random)
             42 LOAD_CONST               0 (0)
             44 LOAD_CONST               1 (None)
             46 IMPORT_NAME              5 (time)
             48 STORE_NAME               5 (time)

  2          50 LOAD_CONST               0 (0)
             52 LOAD_CONST               1 (None)
             54 IMPORT_NAME              6 (datetime)
             56 STORE_NAME               6 (datetime)

  3          58 LOAD_CONST               0 (0)
             60 LOAD_CONST               2 (('track',))
             62 IMPORT_NAME              7 (rich.progress)
             64 IMPORT_FROM              8 (track)
             66 STORE_NAME               8 (track)
             68 POP_TOP

  4          70 LOAD_CONST               0 (0)
             72 LOAD_CONST               3 (('sleep',))
             74 IMPORT_NAME              5 (time)
             76 IMPORT_FROM              9 (sleep)
             78 STORE_NAME               9 (sleep)
             80 POP_TOP

  5          82 LOAD_CONST               0 (0)
             84 LOAD_CONST               1 (None)
             86 IMPORT_NAME             10 (getpass)
             88 STORE_NAME              10 (getpass)

  6          90 LOAD_CONST               0 (0)
             92 LOAD_CONST               4 (('system',))
             94 IMPORT_NAME              0 (os)
             96 IMPORT_FROM             11 (system)
             98 STORE_NAME              12 (psl)
            100 POP_TOP

  7         102 LOAD_CONST               0 (0)
            104 LOAD_CONST               5 (('BeautifulSoup',))
            106 IMPORT_NAME             13 (bs4)
            108 IMPORT_FROM             14 (BeautifulSoup)
            110 STORE_NAME              15 (sop)
            112 POP_TOP

  8         114 LOAD_CONST               0 (0)
            116 LOAD_CONST               6 (('ThreadPoolExecutor',))
            118 IMPORT_NAME             16 (concurrent.futures)
            120 IMPORT_FROM             17 (ThreadPoolExecutor)
            122 STORE_NAME              18 (bsn)
            124 POP_TOP

  9         126 LOAD_CONST               0 (0)
            128 LOAD_CONST               1 (None)
            130 IMPORT_NAME              0 (os)
            132 STORE_NAME               0 (os)

 10         134 LOAD_CONST               0 (0)
            136 LOAD_CONST               7 (('response',))
            138 IMPORT_NAME             19 (urllib)
            140 IMPORT_FROM             20 (response)
            142 STORE_NAME              20 (response)
            144 POP_TOP

 11         146 LOAD_CONST               0 (0)
            148 LOAD_CONST               1 (None)
            150 IMPORT_NAME             21 (mechanize)
            152 STORE_NAME              21 (mechanize)

 12         154 LOAD_CONST               0 (0)
            156 LOAD_CONST               1 (None)
            158 IMPORT_NAME              0 (os)
            160 STORE_NAME               0 (os)

 13         162 LOAD_CONST               0 (0)
            164 LOAD_CONST               1 (None)
            166 IMPORT_NAME              2 (requests)
            168 STORE_NAME               2 (requests)
            170 LOAD_CONST               0 (0)
            172 LOAD_CONST               1 (None)
            174 IMPORT_NAME              5 (time)
            176 STORE_NAME               5 (time)

 14         178 LOAD_CONST               0 (0)
            180 LOAD_CONST               3 (('sleep',))
            182 IMPORT_NAME              5 (time)
            184 IMPORT_FROM              9 (sleep)
            186 STORE_NAME               9 (sleep)
            188 POP_TOP

 15         190 LOAD_CONST               0 (0)
            192 LOAD_CONST               1 (None)
            194 IMPORT_NAME              6 (datetime)
            196 STORE_NAME               6 (datetime)

 16         198 LOAD_CONST               0 (0)
            200 LOAD_CONST               1 (None)
            202 IMPORT_NAME              1 (sys)
            204 STORE_NAME               1 (sys)

 17         206 PUSH_NULL
            208 LOAD_NAME               22 (print)
            210 LOAD_CONST               8 ('\x1b[1;32m[•] \x1b[1;33mJOIN MY FACEBOOK GROUP....!')
            212 PRECALL                  1
            216 CALL                     1
            226 POP_TOP

 18         228 PUSH_NULL
            230 LOAD_NAME                0 (os)
            232 LOAD_ATTR               11 (system)
            242 LOAD_CONST               9 ('xdg-open https://www.facebook.com/groups/647866620424527/?mibextid=ZbWKwL')
            244 PRECALL                  1
            248 CALL                     1
            258 POP_TOP

 19         260 PUSH_NULL
            262 LOAD_NAME               22 (print)
            264 LOAD_CONST              10 ('\x1b[92;1m>>\x1b[1;37m Installing missing modules ...')
            266 PRECALL                  1
            270 CALL                     1
            280 POP_TOP

 20         282 PUSH_NULL
            284 LOAD_NAME                0 (os)
            286 LOAD_ATTR               11 (system)
            296 LOAD_CONST              11 ('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
            298 PRECALL                  1
            302 CALL                     1
            312 POP_TOP

 21         314 PUSH_NULL
            316 LOAD_NAME               12 (psl)
            318 LOAD_CONST              12 ('rm -rf filer.txt')
            320 PRECALL                  1
            324 CALL                     1
            334 POP_TOP

 22         336 BUILD_LIST               0
            338 STORE_NAME              23 (idd)

 23         340 PUSH_NULL
            342 LOAD_NAME                0 (os)
            344 LOAD_ATTR               11 (system)
            354 LOAD_CONST              13 ('clear')
            356 PRECALL                  1
            360 CALL                     1
            370 POP_TOP

 24         372 LOAD_CONST              14 ('\n[•] \x1b[1;92m███╗   ███╗   ██╗  ██╗████████╗██████╗ \n[•] \x1b[1;97m████╗ ████║   ██║  ██║╚══██╔══╝██╔══██╗\n[•] \x1b[1;94m██╔████╔██║   ███████║   ██║   ██████╔╝\n[•] \x1b[1;91m██║╚██╔╝██║   ██╔══██║   ██║   ██╔══██╗\n[•] \x1b[1;96m██║ ╚═╝ ██║██╗██║  ██║██╗██║██╗██████╔╝\n[•] \x1b[1;97m╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝╚═════╝ \n   \n\x1b[1;37m=====================================\n[•]  \x1b[1;36m𝗢𝗪𝗡3𝗥         : \x1b[1;37m𝗠9𝗛𝗧9𝗕 𝘅 𝗦𝗔𝗜𝗙𝗨\n[•]  \x1b[1;32m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞      : \x1b[1;32m𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗\n[•]  \x1b[1;32m𝗧𝗢𝗢𝗟𝗦 𝗦𝗧𝗔𝗧𝗨𝗦  : \x1b[1;32m𝗙𝗥𝗘𝗘 \n[•]  \x1b[1;32m𝗖𝗥𝗘𝗔𝗧𝗘𝗥 𝗕𝗬    : \x1b[1;37m𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗\n\x1b[1;37m=====================================\n')
            374 STORE_NAME              24 (logo)

 39         376 PUSH_NULL
            378 LOAD_NAME               12 (psl)
            380 LOAD_CONST              12 ('rm -rf filer.txt')
            382 PRECALL                  1
            386 CALL                     1
            396 POP_TOP

 40         398 BUILD_LIST               0
            400 STORE_NAME              23 (idd)

 41         402 LOAD_CONST              15 (<code object lines at 0x777e45d1b0, file "", line 41>)
            404 MAKE_FUNCTION            0
            406 STORE_NAME              25 (lines)

 43         408 LOAD_CONST              16 (<code object main at 0x78fe66aea0, file "", line 43>)
            410 MAKE_FUNCTION            0
            412 STORE_NAME              26 (main)

 76         414 PUSH_NULL
            416 LOAD_NAME               26 (main)
            418 PRECALL                  0
            422 CALL                     0
            432 POP_TOP

 78         434 LOAD_CONST              17 (<code object menu at 0x791e65d070, file "", line 78>)
            436 MAKE_FUNCTION            0
            438 STORE_NAME              27 (menu)

134         440 LOAD_CONST              18 (<code object md at 0x792e658c70, file "", line 134>)
            442 MAKE_FUNCTION            0
            444 STORE_NAME              28 (md)

193         446 LOAD_CONST              19 (<code object msg at 0x791e65e900, file "", line 193>)
            448 MAKE_FUNCTION            0
            450 STORE_NAME              29 (msg)

282         452 LOAD_CONST              20 (<code object cpy at 0x777e5fdcb0, file "", line 282>)
            454 MAKE_FUNCTION            0
            456 STORE_NAME              30 (cpy)

290         458 LOAD_CONST              21 (<code object m3 at 0x791e667430, file "", line 290>)
            460 MAKE_FUNCTION            0
            462 STORE_NAME              31 (m3)

419         464 LOAD_CONST              22 (<code object m4 at 0x791e662a80, file "", line 419>)
            466 MAKE_FUNCTION            0
            468 STORE_NAME              32 (m4)

573         470 LOAD_CONST              23 (<code object m2 at 0x790e66c860, file "", line 573>)
            472 MAKE_FUNCTION            0
            474 STORE_NAME              33 (m2)

650         476 LOAD_CONST              24 (<code object pst at 0x792e65a090, file "", line 650>)
            478 MAKE_FUNCTION            0
            480 STORE_NAME              34 (pst)

787         482 LOAD_CONST              25 (<code object approval at 0x790e670250, file "", line 787>)
            484 MAKE_FUNCTION            0
            486 STORE_NAME              35 (approval)

830         488 PUSH_NULL
            490 LOAD_NAME               35 (approval)
            492 PRECALL                  0
            496 CALL                     0
            506 POP_TOP
            508 LOAD_CONST               1 (None)
            510 RETURN_VALUE

Disassembly of <code object lines at 0x777e45d1b0, file "", line 41>:
 41           0 RESUME                   0

 42           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('\x1b[1;37m-------------------------------------------')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

Disassembly of <code object main at 0x78fe66aea0, file "", line 43>:
 43           0 RESUME                   0

 44           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_GLOBAL              2 (logo)
             26 PRECALL                  1
             30 CALL                     1
             40 POP_TOP

 45          42 LOAD_GLOBAL              1 (NULL + print)
             54 LOAD_CONST               1 ('\x1b[1;31m  \x1b[1;47m WELLCOME TO √ M.H.T.B TOOLS \x1b[0m')
             56 PRECALL                  1
             60 CALL                     1
             70 POP_TOP

 46          72 LOAD_GLOBAL              1 (NULL + print)
             84 LOAD_CONST               2 ('')
             86 PRECALL                  1
             90 CALL                     1
            100 POP_TOP

 47         102 LOAD_GLOBAL              1 (NULL + print)
            114 LOAD_CONST               3 ('\x1b[1;37m  \x1b[1;41m 𝙏𝙊𝙊𝙇𝙎 𝙊𝙒𝙉𝙀𝙍 𝙈𝘼𝙃𝙏𝘼𝘽 𝘼𝙃𝙈𝘼𝘿 𝙄𝙉𝘿𝙄𝘼𝙉 \x1b[0m')
            116 PRECALL                  1
            120 CALL                     1
            130 POP_TOP

 48         132 LOAD_GLOBAL              1 (NULL + print)
            144 LOAD_CONST               2 ('')
            146 PRECALL                  1
            150 CALL                     1
            160 POP_TOP

 49         162 LOAD_GLOBAL              1 (NULL + print)
            174 LOAD_CONST               4 ('- - - - - - - - - - - - - - - - - - - - - - -')
            176 PRECALL                  1
            180 CALL                     1
            190 POP_TOP

 50         192 LOAD_GLOBAL              1 (NULL + print)
            204 LOAD_CONST               5 ('\x1b[1;37m \x1b[1;41m 𝙁𝙍𝙀𝙀 𝘼𝙋𝙋𝙍𝙊𝙑𝘼𝙇 𝙎𝙀𝙉𝙏 𝙁𝙍𝙄𝙀𝙉𝘿 𝙍𝙀𝙌𝙐𝙀𝙎𝙏 𝙈𝙔 𝙄𝘿 \x1b[0m')
            206 PRECALL                  1
            210 CALL                     1
            220 POP_TOP

 51         222 LOAD_GLOBAL              1 (NULL + print)
            234 LOAD_CONST               6 ('- - - - - - - - - - - - - - -- -- - - - - - - ')
            236 PRECALL                  1
            240 CALL                     1
            250 POP_TOP

 54         252 LOAD_GLOBAL              1 (NULL + print)
            264 LOAD_CONST               2 ('')
            266 PRECALL                  1
            270 CALL                     1
            280 POP_TOP

 55         282 LOAD_GLOBAL              1 (NULL + print)
            294 LOAD_CONST               7 ('\x1b[1;32m [1] 𝙁𝙄𝙍𝙎𝙏 𝙎𝙀𝙉𝙏 𝙁𝙍𝙄𝙀𝙉𝘿 𝙍𝙀𝙌𝙐𝙀𝙎𝙏  ')
            296 PRECALL                  1
            300 CALL                     1
            310 POP_TOP

 56         312 LOAD_GLOBAL              1 (NULL + print)
            324 LOAD_CONST               8 ('\x1b[1;33m [2] 𝗘𝙓𝙄𝙏 ')            326 PRECALL                  1
            330 CALL                     1
            340 POP_TOP

 57         342 LOAD_GLOBAL              1 (NULL + print)
            354 LOAD_CONST               9 ('≪━─━─━─━─━─━─━─━──━─━─━─━─━─━─━─━─━─━─━─━≫')
            356 PRECALL                  1
            360 CALL                     1
            370 POP_TOP

 58         372 LOAD_GLOBAL              5 (NULL + input)
            384 LOAD_CONST              10 ('\x1b[1;37m Choose : ')            386 PRECALL                  1
            390 CALL                     1
            400 STORE_FAST               0 (Baloch)

 59         402 LOAD_FAST                0 (Baloch)
            404 LOAD_CONST              11 (('', ' '))
            406 CONTAINS_OP              0
            408 POP_JUMP_FORWARD_IF_FALSE    16 (to 442)

 60         410 LOAD_GLOBAL              7 (NULL + exit)
            422 PRECALL                  0
            426 CALL                     0
            436 POP_TOP
            438 LOAD_CONST               0 (None)
            440 RETURN_VALUE

 61     >>  442 LOAD_FAST                0 (Baloch)
            444 LOAD_CONST              12 (('2', '02'))
            446 CONTAINS_OP              0
            448 POP_JUMP_FORWARD_IF_FALSE    31 (to 512)

 62         450 LOAD_GLOBAL              1 (NULL + print)
            462 LOAD_CONST              13 ('    Thanks Dear ♥️')
            464 PRECALL                  1
            468 CALL                     1
            478 POP_TOP

 63         480 LOAD_GLOBAL              7 (NULL + exit)
            492 PRECALL                  0
            496 CALL                     0
            506 POP_TOP
            508 LOAD_CONST               0 (None)
            510 RETURN_VALUE

 64     >>  512 LOAD_FAST                0 (Baloch)
            514 LOAD_CONST              14 (('1', '01'))
            516 CONTAINS_OP              0
            518 POP_JUMP_FORWARD_IF_FALSE   154 (to 828)

 65         520 LOAD_GLOBAL              9 (NULL + os)
            532 LOAD_ATTR                5 (system)
            542 LOAD_CONST              15 ('xdg-open https://www.facebook.com/SK.ALI.MAHTAB.AHMAD.INDIA ')
            544 PRECALL                  1
            548 CALL                     1
            558 POP_TOP

 66         560 LOAD_GLOBAL              1 (NULL + print)
            572 LOAD_CONST               2 ('')
            574 PRECALL                  1
            578 CALL                     1
            588 POP_TOP

 68         590 LOAD_GLOBAL              1 (NULL + print)
            602 LOAD_CONST              16 (' \x1b[1;92m𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗔𝗣𝗣𝗥𝗢𝗩𝗔𝗟 ')
            604 PRECALL                  1
            608 CALL                     1
            618 POP_TOP

 69         620 LOAD_GLOBAL              1 (NULL + print)
            632 LOAD_CONST               2 ('')
            634 PRECALL                  1
            638 CALL                     1
            648 POP_TOP

 70         650 LOAD_GLOBAL              5 (NULL + input)
            662 LOAD_CONST              17 ('\x1b[1;33m TYPE THE OWNER FACEBOOK ACCOUNT NAME :\x1b[1;0m\x1b[1;37m')
            664 PRECALL                  1
            668 CALL                     1
            678 POP_TOP

 71         680 NOP

 72         682 LOAD_GLOBAL              1 (NULL + print)
            694 LOAD_CONST               2 ('')
            696 PRECALL                  1
            700 CALL                     1
            710 POP_TOP

 73         712 LOAD_GLOBAL              1 (NULL + print)
            724 LOAD_CONST              18 ('\x1b[1;32m WELCOME ••𝘔𝘈𝘏𝘛𝘈𝘉•• BRAND TOOLS')
            726 PRECALL                  1
            730 CALL                     1
            740 POP_TOP
            742 LOAD_GLOBAL             13 (NULL + time)
            754 LOAD_ATTR                7 (sleep)
            764 LOAD_CONST              19 (5)
            766 PRECALL                  1
            770 CALL                     1
            780 POP_TOP

 74         782 NOP

 75         784 LOAD_GLOBAL              9 (NULL + os)
            796 LOAD_ATTR                5 (system)
            806 LOAD_CONST              20 ('clear')
            808 PRECALL                  1
            812 CALL                     1
            822 POP_TOP
            824 LOAD_CONST               0 (None)
            826 RETURN_VALUE

 64     >>  828 LOAD_CONST               0 (None)
            830 RETURN_VALUE

Disassembly of <code object menu at 0x791e65d070, file "", line 78>:
 78           0 RESUME                   0

 79           2 LOAD_GLOBAL              1 (NULL + os)
             14 LOAD_ATTR                1 (system)
             24 LOAD_CONST               1 ('clear')
             26 PRECALL                  1
             30 CALL                     1
             40 POP_TOP

 80          42 LOAD_GLOBAL              5 (NULL + print)
             54 LOAD_GLOBAL              6 (logo)
             66 PRECALL                  1
             70 CALL                     1
             80 POP_TOP

 81          82 LOAD_GLOBAL              5 (NULL + print)
             94 LOAD_CONST               2 ('\x1b[1;37m\x1b[1;41m 𝗖𝗥𝗘𝗔𝗧𝗘𝗥  𝗕𝗬 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
             96 PRECALL                  1
            100 CALL                     1
            110 POP_TOP

 82         112 LOAD_GLOBAL              5 (NULL + print)
            124 LOAD_CONST               3 ('--------------------------------')
            126 PRECALL                  1
            130 CALL                     1
            140 POP_TOP

 83         142 LOAD_GLOBAL              5 (NULL + print)
            154 LOAD_CONST               4 ('[01]\x1b[1;32m LOADER COOKIE LOGIN ')
            156 PRECALL                  1
            160 CALL                     1
            170 POP_TOP

 84         172 LOAD_GLOBAL              5 (NULL + print)
            184 LOAD_CONST               5 ('[02]\x1b[1;32m LOADER TOKKEN LOGIN')
            186 PRECALL                  1
            190 CALL                     1
            200 POP_TOP

 85         202 LOAD_GLOBAL              5 (NULL + print)
            214 LOAD_CONST               6 ('[03]\x1b[1;32m BINA 2FACTOR ID LOGIN')
            216 PRECALL                  1
            220 CALL                     1
            230 POP_TOP

 86         232 LOAD_GLOBAL              5 (NULL + print)
            244 LOAD_CONST               7 ('[04]\x1b[1;32m 2FCTOR ID[\x1b[1;37m LOGIN]')
            246 PRECALL                  1
            250 CALL                     1
            260 POP_TOP

 87         262 LOAD_GLOBAL              5 (NULL + print)
            274 LOAD_CONST               8 ('[05]\x1b[1;32m POST  LOAD3R  LOGIN')
            276 PRECALL                  1
            280 CALL                     1
            290 POP_TOP

 88         292 LOAD_GLOBAL              5 (NULL + print)
            304 LOAD_CONST               9 ('[06]\x1b[1;32m AUTO POST COMMENT')
            306 PRECALL                  1
            310 CALL                     1
            320 POP_TOP

 89         322 LOAD_GLOBAL              5 (NULL + print)
            334 LOAD_CONST              10 ('[07]\x1b[1;32m FACEBOOK AUTO  SHARE')
            336 PRECALL                  1
            340 CALL                     1
            350 POP_TOP

 90         352 LOAD_GLOBAL              5 (NULL + print)
            364 LOAD_CONST              11 ('[08]\x1b[1;32m MAHTAB   LO9DER')
            366 PRECALL                  1
            370 CALL                     1
            380 POP_TOP

 91         382 LOAD_GLOBAL              5 (NULL + print)
            394 LOAD_CONST              12 ('[09]\x1b[1;32m FACEBOOK ID CLONE ')
            396 PRECALL                  1
            400 CALL                     1
            410 POP_TOP

 92         412 LOAD_GLOBAL              5 (NULL + print)
            424 LOAD_CONST              13 ('[10]\x1b[1;32m FB TOKEN GERNET')
            426 PRECALL                  1
            430 CALL                     1
            440 POP_TOP

 93         442 LOAD_GLOBAL              5 (NULL + print)
            454 LOAD_CONST              14 ('[11]\x1b[1;33m CONTACT TO OWNER')
            456 PRECALL                  1
            460 CALL                     1
            470 POP_TOP

 94         472 LOAD_GLOBAL              5 (NULL + print)
            484 LOAD_CONST              15 ('[00]\x1b[1;31m EXIT')
            486 PRECALL                  1
            490 CALL                     1
            500 POP_TOP

 95         502 LOAD_GLOBAL              5 (NULL + print)
            514 LOAD_CONST              16 ('\x1b[1;37m--------------------------------')
            516 PRECALL                  1
            520 CALL                     1
            530 POP_TOP

 96         532 LOAD_GLOBAL              9 (NULL + input)
            544 LOAD_CONST              17 ('[?] Choose : ')
            546 PRECALL                  1
            550 CALL                     1
            560 STORE_FAST               0 (opt)

 97         562 LOAD_FAST                0 (opt)
            564 LOAD_CONST              18 ('1')
            566 COMPARE_OP               2 (==)
            572 POP_JUMP_FORWARD_IF_FALSE    36 (to 646)

 98         574 LOAD_GLOBAL              1 (NULL + os)
            586 LOAD_ATTR                1 (system)
            596 LOAD_CONST              19 ('xdg-open https://youtube.com/@Skali470')
            598 PRECALL                  1
            602 CALL                     1
            612 POP_TOP

 99         614 LOAD_GLOBAL             11 (NULL + md)
            626 PRECALL                  0
            630 CALL                     0
            640 POP_TOP
            642 LOAD_CONST               0 (None)
            644 RETURN_VALUE

100     >>  646 LOAD_FAST                0 (opt)
            648 LOAD_CONST              20 ('2')
            650 COMPARE_OP               2 (==)
            656 POP_JUMP_FORWARD_IF_FALSE    36 (to 730)

101         658 LOAD_GLOBAL              1 (NULL + os)
            670 LOAD_ATTR                1 (system)
            680 LOAD_CONST              21 ('xdg-open https://www.facebook.com/SK.ALI.MAHTAB.AHMAD.INDIA?mibextid=D4KYlr')
            682 PRECALL                  1
            686 CALL                     1
            696 POP_TOP

102         698 LOAD_GLOBAL             13 (NULL + m2)
            710 PRECALL                  0
            714 CALL                     0
            724 POP_TOP
            726 LOAD_CONST               0 (None)
            728 RETURN_VALUE

103     >>  730 LOAD_FAST                0 (opt)
            732 LOAD_CONST              22 ('3')
            734 COMPARE_OP               2 (==)
            740 POP_JUMP_FORWARD_IF_FALSE    16 (to 774)

104         742 LOAD_GLOBAL             15 (NULL + m3)
            754 PRECALL                  0
            758 CALL                     0
            768 POP_TOP
            770 LOAD_CONST               0 (None)
            772 RETURN_VALUE

105     >>  774 LOAD_FAST                0 (opt)
            776 LOAD_CONST              23 ('4')
            778 COMPARE_OP               2 (==)
            784 POP_JUMP_FORWARD_IF_FALSE    16 (to 818)

106         786 LOAD_GLOBAL             17 (NULL + m4)
            798 PRECALL                  0
            802 CALL                     0
            812 POP_TOP
            814 LOAD_CONST               0 (None)
            816 RETURN_VALUE

107     >>  818 LOAD_FAST                0 (opt)
            820 LOAD_CONST              24 ('5')
            822 COMPARE_OP               2 (==)
            828 POP_JUMP_FORWARD_IF_FALSE    16 (to 862)

108         830 LOAD_GLOBAL             19 (NULL + pst)
            842 PRECALL                  0
            846 CALL                     0
            856 POP_TOP
            858 LOAD_CONST               0 (None)
            860 RETURN_VALUE

109     >>  862 LOAD_FAST                0 (opt)
            864 LOAD_CONST              25 ('6')
            866 COMPARE_OP               2 (==)
            872 POP_JUMP_FORWARD_IF_FALSE    42 (to 958)

110         874 LOAD_GLOBAL              1 (NULL + os)
            886 LOAD_ATTR                1 (system)
            896 LOAD_CONST              26 ('cd && git clone https://github.com/SK-BAAP-786/AUTO-COMMENT')
            898 PRECALL                  1
            902 CALL                     1
            912 POP_TOP

111         914 LOAD_GLOBAL              1 (NULL + os)
            926 LOAD_ATTR                1 (system)
            936 LOAD_CONST              27 ('cd && cd AUTO-COMMENT;git pull;python Auto-comment.py')
            938 PRECALL                  1
            942 CALL                     1
            952 POP_TOP
            954 LOAD_CONST               0 (None)
            956 RETURN_VALUE

112     >>  958 LOAD_FAST                0 (opt)
            960 LOAD_CONST              28 ('7')
            962 COMPARE_OP               2 (==)
            968 POP_JUMP_FORWARD_IF_FALSE    42 (to 1054)

113         970 LOAD_GLOBAL              1 (NULL + os)
            982 LOAD_ATTR                1 (system)
            992 LOAD_CONST              29 ('cd && git clone https://github.com/SK-BAAP-786/Facebook_auto_share.git')
            994 PRECALL                  1
            998 CALL                     1
           1008 POP_TOP

114        1010 LOAD_GLOBAL              1 (NULL + os)
           1022 LOAD_ATTR                1 (system)
           1032 LOAD_CONST              30 ('cd && cd Facebook_auto_share;git pull;python Fb-Auto_share.py')
           1034 PRECALL                  1
           1038 CALL                     1
           1048 POP_TOP
           1050 LOAD_CONST               0 (None)
           1052 RETURN_VALUE

115     >> 1054 LOAD_FAST                0 (opt)
           1056 LOAD_CONST              31 ('8')
           1058 COMPARE_OP               2 (==)
           1064 POP_JUMP_FORWARD_IF_FALSE    42 (to 1150)

116        1066 LOAD_GLOBAL              1 (NULL + os)
           1078 LOAD_ATTR                1 (system)
           1088 LOAD_CONST              32 ('cd && git clone https://github.com/SK-BAAP-786/Fb-L09DER.git ')
           1090 PRECALL                  1
           1094 CALL                     1
           1104 POP_TOP

117        1106 LOAD_GLOBAL              1 (NULL + os)
           1118 LOAD_ATTR                1 (system)
           1128 LOAD_CONST              33 ('cd && cd Fb-L09DER;git pull;python M9HT9B1.py')
           1130 PRECALL                  1
           1134 CALL                     1
           1144 POP_TOP
           1146 LOAD_CONST               0 (None)
           1148 RETURN_VALUE

118     >> 1150 LOAD_FAST                0 (opt)
           1152 LOAD_CONST              34 ('9')
           1154 COMPARE_OP               2 (==)
           1160 POP_JUMP_FORWARD_IF_FALSE    42 (to 1246)

119        1162 LOAD_GLOBAL              1 (NULL + os)
           1174 LOAD_ATTR                1 (system)
           1184 LOAD_CONST              35 ('cd && git clone https://github.com/SK-BAAP-786/LOL2.git')
           1186 PRECALL                  1
           1190 CALL                     1
           1200 POP_TOP

120        1202 LOAD_GLOBAL              1 (NULL + os)
           1214 LOAD_ATTR                1 (system)
           1224 LOAD_CONST              36 ('cd && cd LOL2;git pull;python usman1.py')
           1226 PRECALL                  1
           1230 CALL                     1
           1240 POP_TOP
           1242 LOAD_CONST               0 (None)
           1244 RETURN_VALUE

121     >> 1246 LOAD_FAST                0 (opt)
           1248 LOAD_CONST              37 ('10')
           1250 COMPARE_OP               2 (==)
           1256 POP_JUMP_FORWARD_IF_FALSE    42 (to 1342)

122        1258 LOAD_GLOBAL              1 (NULL + os)
           1270 LOAD_ATTR                1 (system)
           1280 LOAD_CONST              38 ('cd && git clone https://github.com/SK-BAAP-786/Token')
           1282 PRECALL                  1
           1286 CALL                     1
           1296 POP_TOP

123        1298 LOAD_GLOBAL              1 (NULL + os)
           1310 LOAD_ATTR                1 (system)
           1320 LOAD_CONST              39 ('cd && cd Token;git pull;python FB-ACCESS-TOKEN.py')
           1322 PRECALL                  1
           1326 CALL                     1
           1336 POP_TOP
           1338 LOAD_CONST               0 (None)
           1340 RETURN_VALUE

124     >> 1342 LOAD_FAST                0 (opt)
           1344 LOAD_CONST              40 ('11')
           1346 COMPARE_OP               2 (==)
           1352 POP_JUMP_FORWARD_IF_FALSE    36 (to 1426)

125        1354 LOAD_GLOBAL              1 (NULL + os)
           1366 LOAD_ATTR                1 (system)
           1376 LOAD_CONST              21 ('xdg-open https://www.facebook.com/SK.ALI.MAHTAB.AHMAD.INDIA?mibextid=D4KYlr')
           1378 PRECALL                  1
           1382 CALL                     1
           1392 POP_TOP

126        1394 LOAD_GLOBAL             21 (NULL + menu)
           1406 PRECALL                  0
           1410 CALL                     0
           1420 POP_TOP
           1422 LOAD_CONST               0 (None)
           1424 RETURN_VALUE

127     >> 1426 LOAD_FAST                0 (opt)
           1428 LOAD_CONST              41 ('0')
           1430 COMPARE_OP               2 (==)
           1436 POP_JUMP_FORWARD_IF_FALSE    17 (to 1472)

128        1438 LOAD_GLOBAL              5 (NULL + print)
           1450 LOAD_CONST              42 ('NIKAL BHOSDIL KE MARDXHOD')
           1452 PRECALL                  1
           1456 CALL                     1
           1466 POP_TOP
           1468 LOAD_CONST               0 (None)
           1470 RETURN_VALUE

130     >> 1472 LOAD_GLOBAL              5 (NULL + print)
           1484 LOAD_CONST              43 ('\n\x1b[1;31mChoose valid option\x1b[0;97m')
           1486 PRECALL                  1
           1490 CALL                     1
           1500 POP_TOP

131        1502 LOAD_GLOBAL             21 (NULL + menu)
           1514 PRECALL                  0
           1518 CALL                     0
           1528 POP_TOP
           1530 LOAD_CONST               0 (None)
           1532 RETURN_VALUE

Disassembly of <code object md at 0x792e658c70, file "", line 134>:134           0 RESUME                   0

135           2 LOAD_GLOBAL              1 (NULL + os)
             14 LOAD_ATTR                1 (system)
             24 LOAD_CONST               1 ('clear')
             26 PRECALL                  1
             30 CALL                     1
             40 POP_TOP

136          42 LOAD_GLOBAL              5 (NULL + print)
             54 LOAD_GLOBAL              6 (logo)
             66 PRECALL                  1
             70 CALL                     1
             80 POP_TOP

137          82 LOAD_GLOBAL              5 (NULL + print)
             94 LOAD_CONST               2 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗔𝗧𝗘𝗥  𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
             96 PRECALL                  1
            100 CALL                     1
            110 POP_TOP

138         112 LOAD_GLOBAL              5 (NULL + print)
            124 LOAD_CONST               3 ('-------------------------------------------')
            126 PRECALL                  1
            130 CALL                     1
            140 POP_TOP

139         142 LOAD_GLOBAL              5 (NULL + print)
            154 LOAD_CONST               4 ('\x1b[1;97m COOKISE SE APNI ID LOGIN KRO ')
            156 PRECALL                  1
            160 CALL                     1
            170 POP_TOP

140         172 LOAD_GLOBAL              5 (NULL + print)
            184 LOAD_CONST               3 ('-------------------------------------------')
            186 PRECALL                  1
            190 CALL                     1
            200 POP_TOP

141         202 LOAD_GLOBAL              9 (NULL + input)
            214 LOAD_CONST               5 ('\x1b[32m [+] Paste Cookies : ')
            216 PRECALL                  1
            220 CALL                     1
            230 STORE_FAST               0 (coki)

142         232 LOAD_CONST               6 ('cookie')
            234 LOAD_FAST                0 (coki)
            236 BUILD_MAP                1
            238 STORE_FAST               1 (cookies)

143         240 LOAD_GLOBAL             11 (NULL + requests)
            252 LOAD_ATTR                6 (get)
            262 LOAD_CONST               7 ('https://mbasic.facebook.com/')
            264 LOAD_FAST                1 (cookies)
            266 KW_NAMES                 8
            268 PRECALL                  2
            272 CALL                     2
            282 STORE_FAST               2 (ch)

144         284 LOAD_CONST               9 ('mbasic_logout_button')            286 LOAD_FAST                2 (ch)
            288 LOAD_ATTR                7 (text)
            298 CONTAINS_OP              0
            300 POP_JUMP_FORWARD_IF_FALSE     1 (to 304)

145         302 JUMP_FORWARD            45 (to 394)

147     >>  304 LOAD_GLOBAL              5 (NULL + print)
            316 LOAD_CONST              10 (' \x1b[1;91mYour Account is on Checkpoint !!! \x1b[1;97m')
            318 PRECALL                  1
            322 CALL                     1
            332 POP_TOP

148         334 LOAD_GLOBAL              0 (os)
            346 LOAD_ATTR                8 (sys)
            356 LOAD_METHOD              9 (exit)
            378 PRECALL                  0
            382 CALL                     0
            392 POP_TOP

149     >>  394 LOAD_GLOBAL             21 (NULL + track)
            406 LOAD_GLOBAL             23 (NULL + range)
            418 LOAD_CONST              11 (3)
            420 PRECALL                  1
            424 CALL                     1
            434 PRECALL                  1
            438 CALL                     1
            448 GET_ITER
        >>  450 FOR_ITER                19 (to 490)
            452 STORE_FAST               3 (step)

150         454 LOAD_GLOBAL             25 (NULL + sleep)
            466 LOAD_CONST              12 (1)
            468 PRECALL                  1
            472 CALL                     1
            482 POP_TOP

151         484 LOAD_FAST                3 (step)
            486 POP_TOP
            488 JUMP_BACKWARD           20 (to 450)

152     >>  490 LOAD_GLOBAL              1 (NULL + os)
            502 LOAD_ATTR                1 (system)
            512 LOAD_CONST               1 ('clear')
            514 PRECALL                  1
            518 CALL                     1
            528 POP_TOP

153         530 LOAD_GLOBAL              5 (NULL + print)
            542 LOAD_GLOBAL              6 (logo)
            554 PRECALL                  1
            558 CALL                     1
            568 POP_TOP

154         570 LOAD_GLOBAL              5 (NULL + print)
            582 LOAD_CONST              13 (' \x1b[1;92m Account Logged in Successfully\x1b[1;97m ')
            584 PRECALL                  1
            588 CALL                     1
            598 POP_TOP

155         600 LOAD_GLOBAL              5 (NULL + print)
            612 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
            614 PRECALL                  1
            618 CALL                     1
            628 POP_TOP

156         630 LOAD_GLOBAL              5 (NULL + print)
            642 LOAD_CONST              15 ('\x1b[33m  [?] Enter The Time Delay In Seconds')
            644 PRECALL                  1
            648 CALL                     1
            658 POP_TOP

157         660 LOAD_GLOBAL              5 (NULL + print)
            672 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
            674 PRECALL                  1
            678 CALL                     1
            688 POP_TOP

158         690 LOAD_GLOBAL             27 (NULL + int)
            702 LOAD_GLOBAL              9 (NULL + input)
            714 LOAD_CONST              16 (' [+] Enter Time : ')
            716 PRECALL                  1
            720 CALL                     1
            730 PRECALL                  1
            734 CALL                     1
            744 STORE_FAST               4 (delay)

159         746 LOAD_GLOBAL              5 (NULL + print)
            758 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
            760 PRECALL                  1
            764 CALL                     1
            774 POP_TOP

160         776 LOAD_GLOBAL              9 (NULL + input)
            788 LOAD_CONST              17 (' [+] Chat/Inbox Link id : ')
            790 PRECALL                  1
            794 CALL                     1
            804 STORE_FAST               5 (lnk)

161         806 LOAD_GLOBAL              5 (NULL + print)
            818 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
            820 PRECALL                  1
            824 CALL                     1
            834 POP_TOP

162         836 LOAD_GLOBAL              5 (NULL + print)
            848 LOAD_CONST              18 ('\x1b[36m [×] Kitni bar gali Repeat krna chahte he')
            850 PRECALL                  1
            854 CALL                     1
            864 POP_TOP

163         866 LOAD_GLOBAL              5 (NULL + print)
            878 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
            880 PRECALL                  1
            884 CALL                     1
            894 POP_TOP

164         896 LOAD_GLOBAL             27 (NULL + int)
            908 LOAD_GLOBAL              9 (NULL + input)
            920 LOAD_CONST              19 ('\x1b[36m [+] Gali Repeat : ')
            922 PRECALL                  1
            926 CALL                     1
            936 PRECALL                  1
            940 CALL                     1
            950 STORE_FAST               6 (lim)

165         952 LOAD_GLOBAL             29 (NULL + psl)
            964 LOAD_CONST               1 ('clear')
            966 PRECALL                  1
            970 CALL                     1
            980 POP_TOP

166         982 LOAD_GLOBAL              5 (NULL + print)
            994 LOAD_GLOBAL              6 (logo)
           1006 PRECALL                  1
           1010 CALL                     1
           1020 POP_TOP

167        1022 LOAD_GLOBAL              5 (NULL + print)
           1034 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
           1036 PRECALL                  1
           1040 CALL                     1
           1050 POP_TOP

168        1052 LOAD_GLOBAL              9 (NULL + input)
           1064 LOAD_CONST              20 ('\x1b[36m [+] You Hatres Name : ')
           1066 PRECALL                  1
           1070 CALL                     1
           1080 STORE_FAST               7 (hater)

169        1082 LOAD_GLOBAL              5 (NULL + print)
           1094 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
           1096 PRECALL                  1
           1100 CALL                     1
           1110 POP_TOP

170        1112 LOAD_GLOBAL              5 (NULL + print)
           1124 LOAD_CONST              21 ('\x1b[1;32m [÷] Enter File Name ')
           1126 PRECALL                  1
           1130 CALL                     1
           1140 POP_TOP

171        1142 LOAD_GLOBAL              5 (NULL + print)
           1154 LOAD_CONST              14 ('\x1b[37m-------------------------------------------')
           1156 PRECALL                  1
           1160 CALL                     1
           1170 POP_TOP

172        1172 LOAD_GLOBAL              9 (NULL + input)
           1184 LOAD_CONST              22 (' [+] Enter File Name : ')
           1186 PRECALL                  1
           1190 CALL                     1
           1200 STORE_FAST               8 (filee)

173        1202 LOAD_GLOBAL             31 (NULL + open)
           1214 LOAD_FAST                8 (filee)
           1216 LOAD_CONST              23 ('r')
           1218 PRECALL                  2
           1222 CALL                     2
           1232 LOAD_METHOD             16 (read)
           1254 PRECALL                  0
           1258 CALL                     0
           1268 STORE_FAST               9 (fileee)

174        1270 LOAD_GLOBAL             35 (NULL + cpy)
           1282 LOAD_FAST                9 (fileee)
           1284 LOAD_FAST                6 (lim)
           1286 PRECALL                  2
           1290 CALL                     2
           1300 POP_TOP

175        1302 LOAD_GLOBAL             31 (NULL + open)
           1314 LOAD_CONST              24 ('filer.txt')
           1316 LOAD_CONST              23 ('r')
           1318 PRECALL                  2
           1322 CALL                     2
           1332 LOAD_METHOD             18 (readlines)
           1354 PRECALL                  0
           1358 CALL                     0
           1368 STORE_FAST              10 (file)

176        1370 LOAD_GLOBAL             38 (idd)
           1382 LOAD_METHOD             20 (append)
           1404 LOAD_FAST               10 (file)
           1406 PRECALL                  1
           1410 CALL                     1
           1420 POP_TOP

177        1422 LOAD_GLOBAL             43 (NULL + bsn)
           1434 LOAD_CONST              25 (30)
           1436 KW_NAMES                26
           1438 PRECALL                  1
           1442 CALL                     1
           1452 BEFORE_WITH
           1454 STORE_FAST              11 (crack)

178        1456 LOAD_GLOBAL             29 (NULL + psl)
           1468 LOAD_CONST               1 ('clear')
           1470 PRECALL                  1
           1474 CALL                     1
           1484 POP_TOP

179        1486 LOAD_GLOBAL              5 (NULL + print)
           1498 LOAD_GLOBAL              6 (logo)
           1510 PRECALL                  1
           1514 CALL                     1
           1524 POP_TOP

180        1526 LOAD_GLOBAL              5 (NULL + print)
           1538 LOAD_CONST              27 ('')
           1540 PRECALL                  1
           1544 CALL                     1
           1554 POP_TOP

181        1556 LOAD_GLOBAL              5 (NULL + print)
           1568 LOAD_CONST              28 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
           1570 PRECALL                  1
           1574 CALL                     1
           1584 POP_TOP

182        1586 LOAD_GLOBAL              5 (NULL + print)
           1598 LOAD_CONST               3 ('-------------------------------------------')
           1600 PRECALL                  1
           1604 CALL                     1
           1614 POP_TOP

183        1616 LOAD_GLOBAL              5 (NULL + print)
           1628 LOAD_CONST              29 ('[×] YOUR TATA NAME ')
           1630 LOAD_FAST                7 (hater)
           1632 BINARY_OP                0 (+)
           1636 PRECALL                  1
           1640 CALL                     1
           1650 POP_TOP

184        1652 LOAD_GLOBAL              5 (NULL + print)
           1664 LOAD_CONST              30 (' \x1b[1;97m[+] TOTAL MESSAGES :\x1b[1;32m %s')
           1666 LOAD_GLOBAL             45 (NULL + len)
           1678 LOAD_FAST               10 (file)
           1680 PRECALL                  1
           1684 CALL                     1
           1694 BINARY_OP                6 (%)
           1698 PRECALL                  1
           1702 CALL                     1
           1712 POP_TOP

185        1714 LOAD_GLOBAL              5 (NULL + print)
           1726 LOAD_CONST              31 (' \x1b[1;97m[×] YOUR PROCESS STARTED IN L09D3R')
           1728 PRECALL                  1
           1732 CALL                     1
           1742 POP_TOP

186        1744 LOAD_GLOBAL              5 (NULL + print)
           1756 LOAD_CONST               3 ('-------------------------------------------')
           1758 PRECALL                  1
           1762 CALL                     1
           1772 POP_TOP

187        1774 LOAD_GLOBAL             38 (idd)
           1786 GET_ITER
        >> 1788 FOR_ITER                41 (to 1872)
           1790 STORE_FAST              12 (mess)

188        1792 LOAD_CONST              32 ('1')
           1794 STORE_FAST              13 (sm)

189        1796 LOAD_FAST               13 (sm)
           1798 LOAD_CONST              32 ('1')
           1800 COMPARE_OP               2 (==)
           1806 POP_JUMP_FORWARD_IF_FALSE    31 (to 1870)

190        1808 LOAD_FAST               11 (crack)
           1810 LOAD_METHOD             23 (submit)
           1832 LOAD_GLOBAL             48 (msg)
           1844 LOAD_FAST               12 (mess)
           1846 LOAD_FAST                0 (coki)
           1848 LOAD_FAST                5 (lnk)
           1850 LOAD_FAST                4 (delay)
           1852 LOAD_FAST                7 (hater)
           1854 PRECALL                  6
           1858 CALL                     6
           1868 POP_TOP
        >> 1870 JUMP_BACKWARD           42 (to 1788)

191     >> 1872 LOAD_GLOBAL              0 (os)
           1884 LOAD_ATTR                8 (sys)
           1894 LOAD_METHOD              9 (exit)
           1916 PRECALL                  0
           1920 CALL                     0
           1930 POP_TOP

177        1932 LOAD_CONST               0 (None)
           1934 LOAD_CONST               0 (None)
           1936 LOAD_CONST               0 (None)
           1938 PRECALL                  2
           1942 CALL                     2
           1952 POP_TOP
           1954 LOAD_CONST               0 (None)
           1956 RETURN_VALUE
        >> 1958 PUSH_EXC_INFO
           1960 WITH_EXCEPT_START
           1962 POP_JUMP_FORWARD_IF_TRUE     4 (to 1972)
           1964 RERAISE                  2
        >> 1966 COPY                     3
           1968 POP_EXCEPT
           1970 RERAISE                  1
        >> 1972 POP_TOP
           1974 POP_EXCEPT
           1976 POP_TOP
           1978 POP_TOP
           1980 LOAD_CONST               0 (None)
           1982 RETURN_VALUE
ExceptionTable:
  1454 to 1930 -> 1958 [1] lasti
  1958 to 1964 -> 1966 [3] lasti
  1972 to 1972 -> 1966 [3] lasti

Disassembly of <code object msg at 0x791e65e900, file "", line 193>:
193           0 RESUME                   0

194           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (Session)
             24 PRECALL                  0
             28 CALL                     0
             38 STORE_FAST               5 (ses)

195          40 NOP

196          42 LOAD_FAST                0 (mess)
             44 GET_ITER
        >>   46 EXTENDED_ARG             2
             48 FOR_ITER               696 (to 1442)
             50 STORE_FAST               6 (msgs)

197          52 NOP

198          54 LOAD_GLOBAL              5 (NULL + time)
             66 LOAD_ATTR                3 (sleep)
             76 LOAD_FAST                3 (delay)
             78 PRECALL                  1
             82 CALL                     1
             92 POP_TOP

199          94 LOAD_GLOBAL              8 (datetime)
            106 LOAD_ATTR                4 (datetime)
            116 LOAD_METHOD              5 (now)
            138 PRECALL                  0
            142 CALL                     0
            152 STORE_FAST               7 (timm)

200         154 LOAD_GLOBAL             13 (NULL + str)
            166 LOAD_FAST                7 (timm)
            168 PRECALL                  1
            172 CALL                     1
            182 LOAD_METHOD              7 (split)
            204 LOAD_CONST               1 (' ')
            206 PRECALL                  1
            210 CALL                     1
            220 UNPACK_SEQUENCE          2
            224 STORE_FAST               8 (nm)
            226 STORE_FAST               9 (ti)

201         228 LOAD_FAST                9 (ti)
            230 LOAD_METHOD              7 (split)
            252 LOAD_CONST               2 ('.')
            254 PRECALL                  1
            258 CALL                     1
            268 UNPACK_SEQUENCE          2
            272 STORE_FAST              10 (tim)
            274 STORE_FAST              11 (hff)

202         276 LOAD_GLOBAL              8 (datetime)
            288 LOAD_ATTR                8 (date)
            298 LOAD_METHOD              9 (today)
            320 PRECALL                  0
            324 CALL                     0
            334 STORE_FAST              12 (today)

203         336 LOAD_GLOBAL             13 (NULL + str)
            348 LOAD_FAST               12 (today)
            350 PRECALL                  1
            354 CALL                     1
            364 LOAD_METHOD              7 (split)
            386 LOAD_CONST               3 ('-')
            388 PRECALL                  1
            392 CALL                     1
            402 UNPACK_SEQUENCE          3
            406 STORE_FAST              13 (year)
            408 STORE_FAST              14 (month)
            410 STORE_FAST              15 (day)

204         412 LOAD_CONST               4 ('cookie')
            414 LOAD_FAST                1 (coki)
            416 BUILD_MAP                1
            418 STORE_FAST              16 (cookies)

205         420 LOAD_CONST               5 ('https://d.facebook.com/messages/read/?tid=')
            422 LOAD_FAST                2 (lnk)
            424 BINARY_OP                0 (+)
            428 STORE_FAST              17 (g_url)

206         430 BUILD_MAP                0

207         432 LOAD_CONST               6 ('authority')
            434 LOAD_CONST               7 ('d.facebook.com')

206         436 MAP_ADD                  1

208         438 LOAD_CONST               8 ('accept')
            440 LOAD_CONST               9 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')

206         442 MAP_ADD                  1

209         444 LOAD_CONST              10 ('accept-language')
            446 LOAD_CONST              11 ('en-US,en;q=0.9')

206         448 MAP_ADD                  1

210         450 LOAD_CONST              12 ('cache-control')
            452 LOAD_CONST              13 ('max-age=0')

206         454 MAP_ADD                  1

211         456 LOAD_CONST              14 ('referer')
            458 LOAD_CONST               5 ('https://d.facebook.com/messages/read/?tid=')
            460 LOAD_FAST                2 (lnk)
            462 BINARY_OP                0 (+)

206         466 MAP_ADD                  1

212         468 LOAD_CONST              15 ('sec-ch-prefers-color-scheme')
            470 LOAD_CONST              16 ('light')

206         472 MAP_ADD                  1

213         474 LOAD_CONST              17 ('sec-ch-ua')
            476 LOAD_CONST              18 ('" Not A;Brand";v="99", "Chromium";v="101"')

206         478 MAP_ADD                  1

214         480 LOAD_CONST              19 ('sec-ch-ua-full-version-list')
            482 LOAD_CONST              20 ('" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"')

206         484 MAP_ADD                  1

215         486 LOAD_CONST              21 ('sec-ch-ua-mobile')
            488 LOAD_CONST              22 ('?1')

206         490 MAP_ADD                  1

216         492 LOAD_CONST              23 ('sec-ch-ua-platform')
            494 LOAD_CONST              24 ('"Android"')

206         496 MAP_ADD                  1

217         498 LOAD_CONST              25 ('sec-ch-ua-platform-version')
            500 LOAD_CONST              26 ('"11.0.0"')

206         502 MAP_ADD                  1

218         504 LOAD_CONST              27 ('sec-fetch-dest')
            506 LOAD_CONST              28 ('document')

206         508 MAP_ADD                  1

219         510 LOAD_CONST              29 ('sec-fetch-mode')
            512 LOAD_CONST              30 ('navigate')

206         514 MAP_ADD                  1

220         516 LOAD_CONST              31 ('sec-fetch-site')
            518 LOAD_CONST              32 ('same-origin')

206         520 MAP_ADD                  1

221         522 LOAD_CONST              33 ('sec-fetch-user')
            524 LOAD_CONST              22 ('?1')

206         526 MAP_ADD                  1

222         528 LOAD_CONST              34 ('upgrade-insecure-requests')
            530 LOAD_CONST              35 ('1')

206         532 MAP_ADD                  1

223         534 LOAD_CONST              36 ('user-agent')
            536 LOAD_CONST              37 ('Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36')

206         538 MAP_ADD                  1
            540 STORE_FAST              18 (g_headers)

225         542 LOAD_GLOBAL              1 (NULL + requests)
            554 LOAD_ATTR               10 (get)
            564 LOAD_FAST               17 (g_url)
            566 LOAD_FAST               16 (cookies)
            568 LOAD_FAST               18 (g_headers)
            570 KW_NAMES                38
            572 PRECALL                  3
            576 CALL                     3
            586 LOAD_ATTR               11 (text)
            596 STORE_FAST              19 (res1)

226         598 LOAD_GLOBAL             25 (NULL + re)
            610 LOAD_ATTR               13 (search)

227         620 LOAD_CONST              39 ('name="jazoest" value="([^"]+)"')

228         622 LOAD_FAST               19 (res1)

226         624 PRECALL                  2
            628 CALL                     2

229         638 LOAD_METHOD             14 (group)
            660 LOAD_CONST              40 (1)
            662 PRECALL                  1
            666 CALL                     1

226         676 STORE_FAST              20 (j2)

231         678 LOAD_GLOBAL             25 (NULL + re)
            690 LOAD_ATTR               13 (search)

232         700 LOAD_CONST              41 ('name="fb_dtsg" value="([^"]+)"')

233         702 LOAD_FAST               19 (res1)

231         704 PRECALL                  2
            708 CALL                     2

234         718 LOAD_METHOD             14 (group)
            740 LOAD_CONST              40 (1)
            742 PRECALL                  1
            746 CALL                     1

231         756 STORE_FAST              21 (fb_dtsg)

236         758 LOAD_GLOBAL             25 (NULL + re)
            770 LOAD_ATTR               13 (search)

237         780 LOAD_CONST              42 ('name="csid" value="([^"]+)"')

238         782 LOAD_FAST               19 (res1)

236         784 PRECALL                  2
            788 CALL                     2

239         798 LOAD_METHOD             14 (group)
            820 LOAD_CONST              40 (1)
            822 PRECALL                  1
            826 CALL                     1

236         836 STORE_FAST              22 (csid)

241         838 LOAD_GLOBAL             25 (NULL + re)
            850 LOAD_ATTR               13 (search)

242         860 LOAD_CONST              43 ('name="tids" value="([^"]+)"')

243         862 LOAD_FAST               19 (res1)

241         864 PRECALL                  2
            868 CALL                     2

244         878 LOAD_METHOD             14 (group)
            900 LOAD_CONST              40 (1)
            902 PRECALL                  1
            906 CALL                     1

241         916 STORE_FAST              23 (tids)

246         918 LOAD_FAST                5 (ses)
            920 LOAD_ATTR               15 (headers)
            930 LOAD_METHOD             16 (update)

247         952 LOAD_CONST              44 ('content-type')
            954 LOAD_CONST              45 ('application/x-www-form-urlencoded')

246         956 BUILD_MAP                1
            958 PRECALL                  1
            962 CALL                     1
            972 POP_TOP

250         974 LOAD_GLOBAL             35 (NULL + sop)
            986 LOAD_FAST               19 (res1)
            988 LOAD_CONST              46 ('html.parser')
            990 PRECALL                  2
            994 CALL                     2
           1004 STORE_FAST              24 (rose1)

251        1006 LOAD_FAST               24 (rose1)
           1008 LOAD_METHOD             18 (find)
           1030 LOAD_CONST              47 ('form')
           1032 LOAD_CONST              48 ('post')
           1034 KW_NAMES                49
           1036 PRECALL                  2
           1040 CALL                     2
           1050 LOAD_CONST              50 ('action')
           1052 BINARY_SUBSCR
           1062 STORE_FAST              25 (rose)

253        1064 LOAD_FAST               21 (fb_dtsg)

254        1066 LOAD_FAST               20 (j2)

255        1068 LOAD_FAST                4 (hater)
           1070 LOAD_CONST               1 (' ')
           1072 BINARY_OP                0 (+)
           1076 LOAD_GLOBAL             13 (NULL + str)
           1088 LOAD_FAST                6 (msgs)
           1090 PRECALL                  1
           1094 CALL                     1
           1104 BINARY_OP                0 (+)

256        1108 LOAD_CONST              51 ('Send')

257        1110 LOAD_FAST               23 (tids)

258        1112 LOAD_CONST              52 ('C3')

259        1114 LOAD_CONST              53 ('')

260        1116 LOAD_CONST              53 ('')

261        1118 LOAD_CONST              53 ('')

262        1120 LOAD_CONST              54 ('legacy')

263        1122 LOAD_FAST               22 (csid)

252        1124 LOAD_CONST              55 (('fb_dtsg', 'jazoest', 'body', 'send', 'tids', 'wwwupp', 'platform_xmd', 'referrer', 'ctype', 'cver', 'csid'))
           1126 BUILD_CONST_KEY_MAP     11
           1128 STORE_FAST              26 (payload)

265        1130 LOAD_CONST              56 ('https://d.facebook.com')
           1132 STORE_FAST              27 (host)

266        1134 LOAD_FAST                5 (ses)
           1136 LOAD_METHOD             19 (post)
           1158 LOAD_FAST               27 (host)
           1160 LOAD_FAST               25 (rose)
           1162 BINARY_OP                0 (+)
           1166 LOAD_FAST               26 (payload)
           1168 LOAD_FAST               16 (cookies)
           1170 KW_NAMES                57
           1172 PRECALL                  3
           1176 CALL                     3
           1186 LOAD_ATTR               11 (text)
           1196 STORE_FAST              28 (post)

267        1198 LOAD_GLOBAL             41 (NULL + print)
           1210 LOAD_CONST              58 (' \x1b[1;97m[+] Date :\x1b[1;96m ')
           1212 LOAD_FAST               15 (day)
           1214 BINARY_OP                0 (+)
           1218 LOAD_CONST              59 ('/')
           1220 BINARY_OP                0 (+)
           1224 LOAD_FAST               14 (month)
           1226 BINARY_OP                0 (+)
           1230 LOAD_CONST              59 ('/')
           1232 BINARY_OP                0 (+)
           1236 LOAD_FAST               13 (year)
           1238 BINARY_OP                0 (+)
           1242 PRECALL                  1
           1246 CALL                     1
           1256 POP_TOP

268        1258 LOAD_GLOBAL             41 (NULL + print)
           1270 LOAD_CONST              60 (' \x1b[1;93m[+] MESG SEND HO GYA:\x1b[1;92m ')
           1272 LOAD_FAST                4 (hater)
           1274 BINARY_OP                0 (+)
           1278 LOAD_FAST                6 (msgs)
           1280 BINARY_OP                0 (+)
           1284 LOAD_CONST              61 ('\x1b[1;97m')
           1286 BINARY_OP                0 (+)
           1290 PRECALL                  1
           1294 CALL                     1
           1304 POP_TOP
           1306 EXTENDED_ARG             2
           1308 JUMP_BACKWARD          632 (to 46)
        >> 1310 PUSH_EXC_INFO

269        1312 LOAD_GLOBAL              0 (requests)
           1324 LOAD_ATTR               21 (exceptions)
           1334 LOAD_ATTR               22 (ConnectionError)
           1344 CHECK_EXC_MATCH
           1346 POP_JUMP_FORWARD_IF_FALSE    24 (to 1396)
           1348 POP_TOP

270        1350 LOAD_GLOBAL              5 (NULL + time)
           1362 LOAD_ATTR                3 (sleep)
           1372 LOAD_CONST              62 (10)
           1374 PRECALL                  1
           1378 CALL                     1
           1388 POP_TOP

271        1390 POP_EXCEPT
           1392 EXTENDED_ARG             2
           1394 JUMP_BACKWARD          675 (to 46)

272     >> 1396 LOAD_GLOBAL             46 (Exception)
           1408 CHECK_EXC_MATCH
           1410 POP_JUMP_FORWARD_IF_FALSE    11 (to 1434)
           1412 STORE_FAST              29 (e)

273        1414 POP_EXCEPT
           1416 LOAD_CONST               0 (None)
           1418 STORE_FAST              29 (e)
           1420 DELETE_FAST             29 (e)
           1422 EXTENDED_ARG             2
           1424 JUMP_BACKWARD          690 (to 46)
           1426 LOAD_CONST               0 (None)
           1428 STORE_FAST              29 (e)
           1430 DELETE_FAST             29 (e)
           1432 RERAISE                  1

272     >> 1434 RERAISE                  0
        >> 1436 COPY                     3
           1438 POP_EXCEPT
           1440 RERAISE                  1

274     >> 1442 LOAD_FAST               30 (loop)
           1444 LOAD_CONST              40 (1)
           1446 BINARY_OP               13 (+=)
           1450 STORE_FAST              30 (loop)
           1452 LOAD_CONST               0 (None)
           1454 RETURN_VALUE
        >> 1456 PUSH_EXC_INFO

275        1458 LOAD_GLOBAL              0 (requests)
           1470 LOAD_ATTR               21 (exceptions)
           1480 LOAD_ATTR               22 (ConnectionError)
           1490 CHECK_EXC_MATCH
           1492 POP_JUMP_FORWARD_IF_FALSE    24 (to 1542)
           1494 POP_TOP

276        1496 LOAD_GLOBAL              5 (NULL + time)
           1508 LOAD_ATTR                3 (sleep)
           1518 LOAD_CONST              62 (10)
           1520 PRECALL                  1
           1524 CALL                     1
           1534 POP_TOP

277        1536 POP_EXCEPT
           1538 LOAD_CONST               0 (None)
           1540 RETURN_VALUE

278     >> 1542 LOAD_GLOBAL             46 (Exception)
           1554 CHECK_EXC_MATCH
           1556 POP_JUMP_FORWARD_IF_FALSE    26 (to 1610)
           1558 STORE_FAST              29 (e)

279        1560 LOAD_GLOBAL             41 (NULL + print)
           1572 LOAD_FAST               29 (e)
           1574 PRECALL                  1
           1578 CALL                     1
           1588 POP_TOP
           1590 POP_EXCEPT
           1592 LOAD_CONST               0 (None)
           1594 STORE_FAST              29 (e)
           1596 DELETE_FAST             29 (e)
           1598 LOAD_CONST               0 (None)
           1600 RETURN_VALUE
        >> 1602 LOAD_CONST               0 (None)
           1604 STORE_FAST              29 (e)
           1606 DELETE_FAST             29 (e)
           1608 RERAISE                  1

278     >> 1610 RERAISE                  0
        >> 1612 COPY                     3
           1614 POP_EXCEPT
           1616 RERAISE                  1
ExceptionTable:
  42 to 50 -> 1456 [0]
  54 to 1304 -> 1310 [1]
  1306 to 1308 -> 1456 [0]
  1310 to 1388 -> 1436 [2] lasti
  1390 to 1394 -> 1456 [0]
  1396 to 1412 -> 1436 [2] lasti
  1414 to 1424 -> 1456 [0]
  1426 to 1434 -> 1436 [2] lasti
  1436 to 1450 -> 1456 [0]
  1456 to 1534 -> 1612 [1] lasti
  1542 to 1558 -> 1612 [1] lasti
  1560 to 1588 -> 1602 [1] lasti
  1602 to 1610 -> 1612 [1] lasti

Disassembly of <code object cpy at 0x777e5fdcb0, file "", line 282>:
282           0 RESUME                   0

283           2 LOAD_GLOBAL              1 (NULL + range)
             14 LOAD_FAST                1 (lim)
             16 PRECALL                  1
             20 CALL                     1
             30 GET_ITER
        >>   32 FOR_ITER                40 (to 114)
             34 STORE_FAST               2 (i)

284          36 LOAD_GLOBAL              3 (NULL + open)
             48 LOAD_CONST               1 ('filer.txt')
             50 LOAD_CONST               2 ('a')
             52 PRECALL                  2
             56 CALL                     2
             66 LOAD_METHOD              2 (write)
             88 LOAD_FAST                0 (fileee)
             90 LOAD_CONST               3 ('\n')
             92 BINARY_OP                0 (+)
             96 PRECALL                  1
            100 CALL                     1
            110 POP_TOP
            112 JUMP_BACKWARD           41 (to 32)

283     >>  114 LOAD_CONST               0 (None)
            116 RETURN_VALUE

Disassembly of <code object m3 at 0x791e667430, file "", line 290>:              0 MAKE_CELL               17 (PASSWORD)
              2 MAKE_CELL               18 (USERNAME)
              4 MAKE_CELL               19 (browser)
              6 MAKE_CELL               20 (datetime)
              8 MAKE_CELL               21 (line)
             10 MAKE_CELL               22 (mechanize)
             12 MAKE_CELL               23 (os)
             14 MAKE_CELL               24 (sleep)
             16 MAKE_CELL               25 (sys)
             18 MAKE_CELL               26 (url)

290          20 RESUME                   0

292          22 LOAD_CONST               1 (0)
             24 LOAD_CONST               2 (('response',))
             26 IMPORT_NAME              0 (urllib)
             28 IMPORT_FROM              1 (response)
             30 STORE_FAST               0 (response)
             32 POP_TOP

293          34 LOAD_CONST               1 (0)
             36 LOAD_CONST               0 (None)
             38 IMPORT_NAME              2 (mechanize)
             40 STORE_DEREF             22 (mechanize)

294          42 LOAD_CONST               1 (0)
             44 LOAD_CONST               0 (None)
             46 IMPORT_NAME              3 (uuid)
             48 STORE_FAST               1 (uuid)

295          50 LOAD_CONST               1 (0)
             52 LOAD_CONST               0 (None)
             54 IMPORT_NAME              4 (os)
             56 STORE_DEREF             23 (os)

296          58 LOAD_CONST               1 (0)
             60 LOAD_CONST               0 (None)
             62 IMPORT_NAME              5 (datetime)
             64 STORE_DEREF             20 (datetime)

297          66 LOAD_CONST               1 (0)
             68 LOAD_CONST               0 (None)
             70 IMPORT_NAME              6 (time)
             72 STORE_FAST               2 (time)

298          74 LOAD_CONST               1 (0)
             76 LOAD_CONST               0 (None)
             78 IMPORT_NAME              7 (sys)
             80 STORE_DEREF             25 (sys)

299          82 LOAD_CONST               1 (0)
             84 LOAD_CONST               3 (('sleep',))
             86 IMPORT_NAME              6 (time)
             88 IMPORT_FROM              8 (sleep)
             90 STORE_DEREF             24 (sleep)
             92 POP_TOP

300          94 PUSH_NULL
             96 LOAD_DEREF              22 (mechanize)
             98 LOAD_ATTR                9 (Browser)
            108 PRECALL                  0
            112 CALL                     0
            122 STORE_DEREF             19 (browser)

301         124 LOAD_DEREF              19 (browser)
            126 LOAD_METHOD             10 (set_handle_robots)
            148 LOAD_CONST               4 (False)
            150 PRECALL                  1
            154 CALL                     1
            164 POP_TOP

302         166 PUSH_NULL
            168 LOAD_DEREF              22 (mechanize)
            170 LOAD_ATTR               11 (CookieJar)
            180 PRECALL                  0
            184 CALL                     0
            194 STORE_FAST               3 (cookies)

303         196 LOAD_DEREF              19 (browser)
            198 LOAD_METHOD             12 (set_cookiejar)
            220 LOAD_FAST                3 (cookies)
            222 PRECALL                  1
            226 CALL                     1
            236 POP_TOP

304         238 LOAD_CONST               5 (('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'))
            240 BUILD_LIST               1
            242 LOAD_DEREF              19 (browser)
            244 STORE_ATTR              13 (addheaders)

305         254 LOAD_DEREF              19 (browser)
            256 LOAD_METHOD             14 (set_handle_refresh)
            278 LOAD_CONST               4 (False)
            280 PRECALL                  1
            284 CALL                     1
            294 POP_TOP

309         296 LOAD_CONST               6 ('https://mbasic.facebook.com/login')
            298 STORE_DEREF             26 (url)

311         300 LOAD_CLOSURE            23 (os)
            302 BUILD_TUPLE              1
            304 LOAD_CONST               7 (<code object clear at 0x777e5b5590, file "", line 311>)
            306 MAKE_FUNCTION            8 (closure)
            308 STORE_FAST               4 (clear)

318         310 LOAD_CLOSURE            24 (sleep)
            312 LOAD_CLOSURE            25 (sys)
            314 BUILD_TUPLE              2
            316 LOAD_CONST               8 (<code object sp at 0x777e5f57f0, file "", line 318>)
            318 MAKE_FUNCTION            8 (closure)
            320 STORE_FAST               5 (sp)

324         322 LOAD_CLOSURE            17 (PASSWORD)
            324 LOAD_CLOSURE            18 (USERNAME)
            326 LOAD_CLOSURE            19 (browser)
            328 LOAD_CLOSURE            26 (url)
            330 BUILD_TUPLE              4
            332 LOAD_CONST               9 (<code object login at 0x78de6585a0, file "", line 324>)
            334 MAKE_FUNCTION            8 (closure)
            336 STORE_FAST               6 (login)

334         338 LOAD_CLOSURE            19 (browser)
            340 BUILD_TUPLE              1
            342 LOAD_CONST              10 (<code object findtextchat at 0x777e474bd0, file "", line 334>)
            344 MAKE_FUNCTION            8 (closure)
            346 STORE_FAST               7 (findtextchat)

347         348 LOAD_CLOSURE            19 (browser)
            350 LOAD_CLOSURE            20 (datetime)
            352 LOAD_CLOSURE            21 (line)
            354 LOAD_CLOSURE            22 (mechanize)
            356 BUILD_TUPLE              4
            358 LOAD_CONST              11 (<code object sendtextconvo at 0x78ee6741b0, file "", line 347>)
            360 MAKE_FUNCTION            8 (closure)
            362 STORE_FAST               8 (sendtextconvo)

363         364 PUSH_NULL
            366 LOAD_DEREF              23 (os)
            368 LOAD_ATTR               15 (system)
            378 LOAD_CONST              12 ('clear')
            380 PRECALL                  1
            384 CALL                     1
            394 POP_TOP

364         396 LOAD_GLOBAL             33 (NULL + print)
            408 LOAD_CONST              13 ('\x1b[1;33;40m')
            410 LOAD_CONST              14 ('')
            412 KW_NAMES                15
            414 PRECALL                  2
            418 CALL                     2
            428 POP_TOP

365         430 LOAD_GLOBAL             33 (NULL + print)
            442 LOAD_GLOBAL             34 (logo)
            454 PRECALL                  1
            458 CALL                     1
            468 POP_TOP

366         470 LOAD_GLOBAL             33 (NULL + print)
            482 LOAD_CONST              16 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
            484 PRECALL                  1
            488 CALL                     1
            498 POP_TOP

367         500 LOAD_GLOBAL             33 (NULL + print)
            512 LOAD_CONST              17 ('-----------------------------------------------')
            514 PRECALL                  1
            518 CALL                     1
            528 POP_TOP

368         530 PUSH_NULL
            532 LOAD_FAST                5 (sp)
            534 LOAD_CONST              18 ('\x1b[1;32m[+] \x1b[1;32mLOGIN FB ID TYP NUMBER & GMAIL AND PASWAD\n')
            536 PRECALL                  1
            540 CALL                     1
            550 POP_TOP

369         552 LOAD_GLOBAL             33 (NULL + print)
            564 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
            566 PRECALL                  1
            570 CALL                     1
            580 POP_TOP

370         582 LOAD_GLOBAL             37 (NULL + str)
            594 LOAD_GLOBAL             39 (NULL + input)
            606 LOAD_CONST              20 ('\x1b[1;32m[+] TYPE NUMBER & GAMIL : ')
            608 PRECALL                  1
            612 CALL                     1
            622 PRECALL                  1
            626 CALL                     1
            636 STORE_DEREF             18 (USERNAME)

371         638 LOAD_GLOBAL             33 (NULL + print)
            650 LOAD_CONST              13 ('\x1b[1;33;40m')
            652 LOAD_CONST              14 ('')
            654 KW_NAMES                15
            656 PRECALL                  2
            660 CALL                     2
            670 POP_TOP

372         672 LOAD_GLOBAL             33 (NULL + print)
            684 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
            686 PRECALL                  1
            690 CALL                     1
            700 POP_TOP

373         702 LOAD_GLOBAL             37 (NULL + str)
            714 LOAD_GLOBAL             39 (NULL + input)
            726 LOAD_CONST              21 ('\x1b[1;32m[?] TYP3 PASWAD: ')
            728 PRECALL                  1
            732 CALL                     1
            742 PRECALL                  1
            746 CALL                     1
            756 STORE_DEREF             17 (PASSWORD)

374         758 PUSH_NULL
            760 LOAD_FAST                6 (login)
            762 PRECALL                  0
            766 CALL                     0
            776 POP_TOP

375         778 LOAD_GLOBAL             33 (NULL + print)
            790 LOAD_CONST              22 ('\x1b[1;34;40m')
            792 LOAD_CONST              14 ('')
            794 KW_NAMES                15
            796 PRECALL                  2
            800 CALL                     2
            810 POP_TOP

376         812 PUSH_NULL
            814 LOAD_DEREF              23 (os)
            816 LOAD_ATTR               15 (system)
            826 LOAD_CONST              12 ('clear')
            828 PRECALL                  1
            832 CALL                     1
            842 POP_TOP

377         844 LOAD_GLOBAL             33 (NULL + print)
            856 LOAD_GLOBAL             34 (logo)
            868 PRECALL                  1
            872 CALL                     1
            882 POP_TOP

378         884 LOAD_GLOBAL             33 (NULL + print)
            896 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
            898 PRECALL                  1
            902 CALL                     1
            912 POP_TOP

379         914 LOAD_GLOBAL             37 (NULL + str)
            926 LOAD_GLOBAL             39 (NULL + input)
            938 LOAD_CONST              23 ('\x1b[1;32m[?] \x1b[1;32mENTER CHET INBOX LINK : ')
            940 PRECALL                  1
            944 CALL                     1
            954 PRECALL                  1
            958 CALL                     1
            968 STORE_FAST               9 (cid)

380         970 LOAD_CONST              24 ('https://mbasic.facebook.com/messages/t/')
            972 LOAD_GLOBAL             37 (NULL + str)
            984 LOAD_FAST                9 (cid)
            986 PRECALL                  1
            990 CALL                     1
           1000 BINARY_OP                0 (+)
           1004 STORE_FAST              10 (curl)

382        1006 LOAD_GLOBAL             33 (NULL + print)
           1018 LOAD_CONST              22 ('\x1b[1;34;40m')
           1020 LOAD_CONST              14 ('')
           1022 KW_NAMES                15
           1024 PRECALL                  2
           1028 CALL                     2
           1038 POP_TOP

383        1040 LOAD_GLOBAL             33 (NULL + print)
           1052 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1054 PRECALL                  1
           1058 CALL                     1
           1068 POP_TOP

384        1070 LOAD_GLOBAL             37 (NULL + str)
           1082 LOAD_GLOBAL             39 (NULL + input)
           1094 LOAD_CONST              25 ('\x1b[1;32m[?] \x1b[1;32mEnter File Name : ')
           1096 PRECALL                  1
           1100 CALL                     1
           1110 PRECALL                  1
           1114 CALL                     1
           1124 STORE_FAST              11 (np)

385        1126 LOAD_GLOBAL             41 (NULL + open)
           1138 LOAD_FAST               11 (np)
           1140 LOAD_CONST              26 ('r')
           1142 PRECALL                  2
           1146 CALL                     2
           1156 STORE_FAST              12 (f)

386        1158 LOAD_FAST               12 (f)
           1160 LOAD_METHOD             21 (readlines)
           1182 PRECALL                  0
           1186 CALL                     0
           1196 STORE_FAST              13 (lines)

387        1198 LOAD_FAST               12 (f)
           1200 LOAD_METHOD             22 (close)
           1222 PRECALL                  0
           1226 CALL                     0
           1236 POP_TOP

388        1238 LOAD_GLOBAL             33 (NULL + print)
           1250 LOAD_CONST              13 ('\x1b[1;33;40m')
           1252 LOAD_CONST              14 ('')
           1254 KW_NAMES                15
           1256 PRECALL                  2
           1260 CALL                     2
           1270 POP_TOP

389        1272 LOAD_GLOBAL             33 (NULL + print)
           1284 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1286 PRECALL                  1
           1290 CALL                     1
           1300 POP_TOP

390        1302 PUSH_NULL
           1304 LOAD_FAST                5 (sp)
           1306 LOAD_CONST              27 ('\x1b[1;32m[?] \x1b[1;32mEnter The Time Delay In Seconds\n')
           1308 PRECALL                  1
           1312 CALL                     1
           1322 POP_TOP

391        1324 LOAD_GLOBAL             33 (NULL + print)
           1336 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1338 PRECALL                  1
           1342 CALL                     1
           1352 POP_TOP

392        1354 LOAD_GLOBAL             47 (NULL + int)
           1366 LOAD_GLOBAL             39 (NULL + input)
           1378 LOAD_CONST              28 ('\x1b[1;32m[?] \x1b[1;32mEnter Time : ')
           1380 PRECALL                  1
           1384 CALL                     1
           1394 PRECALL                  1
           1398 CALL                     1
           1408 STORE_FAST              14 (t)

394        1410 PUSH_NULL
           1412 LOAD_DEREF              23 (os)
           1414 LOAD_ATTR               15 (system)
           1424 LOAD_CONST              12 ('clear')
           1426 PRECALL                  1
           1430 CALL                     1
           1440 POP_TOP

395        1442 LOAD_GLOBAL             33 (NULL + print)
           1454 LOAD_GLOBAL             34 (logo)
           1466 PRECALL                  1
           1470 CALL                     1
           1480 POP_TOP

396        1482 LOAD_GLOBAL             33 (NULL + print)
           1494 LOAD_CONST              16 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
           1496 PRECALL                  1
           1500 CALL                     1
           1510 POP_TOP

397        1512 LOAD_GLOBAL             33 (NULL + print)
           1524 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1526 PRECALL                  1
           1530 CALL                     1
           1540 POP_TOP

398        1542 LOAD_CONST               1 (0)
           1544 STORE_FAST              15 (count)

399        1546 NOP

400     >> 1548 NOP

401        1550 LOAD_FAST               13 (lines)
           1552 GET_ITER
        >> 1554 FOR_ITER               110 (to 1776)
           1556 STORE_DEREF             21 (line)

402        1558 LOAD_GLOBAL             49 (NULL + len)
           1570 LOAD_DEREF              21 (line)
           1572 PRECALL                  1
           1576 CALL                     1
           1586 LOAD_CONST              30 (3)
           1588 COMPARE_OP               4 (>)
           1594 POP_JUMP_FORWARD_IF_FALSE    89 (to 1774)

403        1596 LOAD_FAST               15 (count)
           1598 LOAD_CONST               1 (0)
           1600 COMPARE_OP               3 (!=)
           1606 POP_JUMP_FORWARD_IF_FALSE    11 (to 1630)

404        1608 PUSH_NULL
           1610 LOAD_DEREF              24 (sleep)
           1612 LOAD_FAST               14 (t)
           1614 PRECALL                  1
           1618 CALL                     1
           1628 POP_TOP

405     >> 1630 PUSH_NULL
           1632 LOAD_FAST                7 (findtextchat)
           1634 LOAD_FAST               10 (curl)
           1636 PRECALL                  1
           1640 CALL                     1
           1650 POP_TOP

406        1652 PUSH_NULL
           1654 LOAD_FAST                8 (sendtextconvo)
           1656 LOAD_DEREF              21 (line)
           1658 PRECALL                  1
           1662 CALL                     1
           1672 POP_TOP

407        1674 LOAD_FAST               15 (count)
           1676 LOAD_CONST              31 (1)
           1678 BINARY_OP               13 (+=)
           1682 STORE_FAST              15 (count)

408        1684 LOAD_FAST               15 (count)
           1686 LOAD_CONST              32 (10)
           1688 BINARY_OP                6 (%)
           1692 LOAD_CONST               1 (0)
           1694 COMPARE_OP               2 (==)
           1700 POP_JUMP_FORWARD_IF_FALSE    36 (to 1774)

409        1702 PUSH_NULL
           1704 LOAD_DEREF              24 (sleep)
           1706 LOAD_CONST              31 (1)
           1708 PRECALL                  1
           1712 CALL                     1
           1722 POP_TOP

410        1724 PUSH_NULL
           1726 LOAD_FAST                4 (clear)
           1728 PRECALL                  0
           1732 CALL                     0
           1742 POP_TOP

411        1744 LOAD_GLOBAL             33 (NULL + print)
           1756 LOAD_CONST              33 ('\x1b[1;32m')
           1758 PRECALL                  1
           1762 CALL                     1
           1772 POP_TOP
        >> 1774 JUMP_BACKWARD          111 (to 1554)

401     >> 1776 JUMP_FORWARD            49 (to 1876)
        >> 1778 PUSH_EXC_INFO

412        1780 LOAD_GLOBAL             50 (Exception)
           1792 CHECK_EXC_MATCH
           1794 POP_JUMP_FORWARD_IF_FALSE    36 (to 1868)
           1796 STORE_FAST              16 (e)

413        1798 LOAD_GLOBAL             33 (NULL + print)
           1810 LOAD_FAST               16 (e)
           1812 PRECALL                  1
           1816 CALL                     1
           1826 POP_TOP

414        1828 PUSH_NULL
           1830 LOAD_DEREF              24 (sleep)
           1832 LOAD_CONST              30 (3)
           1834 PRECALL                  1
           1838 CALL                     1
           1848 POP_TOP
           1850 POP_EXCEPT
           1852 LOAD_CONST               0 (None)
           1854 STORE_FAST              16 (e)
           1856 DELETE_FAST             16 (e)
           1858 JUMP_FORWARD             8 (to 1876)
        >> 1860 LOAD_CONST               0 (None)
           1862 STORE_FAST              16 (e)
           1864 DELETE_FAST             16 (e)
           1866 RERAISE                  1

412     >> 1868 RERAISE                  0
        >> 1870 COPY                     3
           1872 POP_EXCEPT
           1874 RERAISE                  1

399     >> 1876 JUMP_BACKWARD          165 (to 1548)
ExceptionTable:
  1550 to 1774 -> 1778 [0]
  1778 to 1796 -> 1870 [1] lasti
  1798 to 1848 -> 1860 [1] lasti
  1860 to 1868 -> 1870 [1] lasti

Disassembly of <code object clear at 0x777e5b5590, file "", line 311>:
              0 COPY_FREE_VARS           1

311           2 RESUME                   0

312           4 LOAD_DEREF               0 (os)
              6 LOAD_ATTR                0 (name)
             16 LOAD_CONST               1 ('nt')
             18 COMPARE_OP               2 (==)
             24 POP_JUMP_FORWARD_IF_FALSE    18 (to 62)

313          26 PUSH_NULL
             28 LOAD_DEREF               0 (os)
             30 LOAD_ATTR                1 (system)
             40 LOAD_CONST               2 ('cls')
             42 PRECALL                  1
             46 CALL                     1
             56 POP_TOP
             58 LOAD_CONST               0 (None)
             60 RETURN_VALUE

315     >>   62 PUSH_NULL
             64 LOAD_DEREF               0 (os)
             66 LOAD_ATTR                1 (system)
             76 LOAD_CONST               3 ('xdg-open ')
             78 PRECALL                  1
             82 CALL                     1
             92 POP_TOP
             94 LOAD_CONST               0 (None)
             96 RETURN_VALUE

Disassembly of <code object sp at 0x777e5f57f0, file "", line 318>:              0 COPY_FREE_VARS           2

318           2 RESUME                   0

319           4 LOAD_FAST                0 (stri)
              6 GET_ITER
        >>    8 FOR_ITER                55 (to 120)
             10 STORE_FAST               1 (letter)

320          12 LOAD_GLOBAL              1 (NULL + print)
             24 LOAD_FAST                1 (letter)
             26 LOAD_CONST               1 ('')
             28 KW_NAMES                 2
             30 PRECALL                  2
             34 CALL                     2
             44 POP_TOP

321          46 LOAD_DEREF               3 (sys)
             48 LOAD_ATTR                1 (stdout)
             58 LOAD_METHOD              2 (flush)
             80 PRECALL                  0
             84 CALL                     0
             94 POP_TOP

322          96 PUSH_NULL
             98 LOAD_DEREF               2 (sleep)
            100 LOAD_CONST               3 (0.03)
            102 PRECALL                  1
            106 CALL                     1
            116 POP_TOP
            118 JUMP_BACKWARD           56 (to 8)

319     >>  120 LOAD_CONST               0 (None)
            122 RETURN_VALUE

Disassembly of <code object login at 0x78de6585a0, file "", line 324>:
              0 COPY_FREE_VARS           4

324           2 RESUME                   0

325           4 LOAD_DEREF               4 (browser)
              6 LOAD_METHOD              0 (open)
             28 LOAD_DEREF               5 (url)
             30 PRECALL                  1
             34 CALL                     1
             44 POP_TOP

326          46 LOAD_DEREF               4 (browser)
             48 LOAD_METHOD              1 (select_form)
             70 LOAD_CONST               1 (0)
             72 KW_NAMES                 2
             74 PRECALL                  1
             78 CALL                     1
             88 POP_TOP

327          90 LOAD_DEREF               3 (USERNAME)
             92 LOAD_DEREF               4 (browser)
             94 LOAD_ATTR                2 (form)
            104 LOAD_CONST               3 ('email')
            106 STORE_SUBSCR

328         110 LOAD_DEREF               2 (PASSWORD)
            112 LOAD_DEREF               4 (browser)
            114 LOAD_ATTR                2 (form)
            124 LOAD_CONST               4 ('pass')
            126 STORE_SUBSCR

329         130 LOAD_DEREF               4 (browser)
            132 LOAD_METHOD              3 (submit)
            154 PRECALL                  0
            158 CALL                     0
            168 STORE_FAST               0 (r)

330         170 LOAD_GLOBAL              1 (NULL + open)
            182 LOAD_CONST               5 ('login.html')
            184 LOAD_CONST               6 ('wb')
            186 PRECALL                  2
            190 CALL                     2
            200 STORE_FAST               1 (f)

331         202 LOAD_FAST                1 (f)
            204 LOAD_METHOD              4 (write)
            226 LOAD_FAST                0 (r)
            228 LOAD_METHOD              5 (read)
            250 PRECALL                  0
            254 CALL                     0
            264 PRECALL                  1
            268 CALL                     1
            278 POP_TOP

332         280 LOAD_DEREF               4 (browser)
            282 LOAD_METHOD              1 (select_form)
            304 LOAD_CONST               1 (0)
            306 KW_NAMES                 2
            308 PRECALL                  1
            312 CALL                     1
            322 POP_TOP

333         324 LOAD_FAST                1 (f)
            326 LOAD_METHOD              6 (close)
            348 PRECALL                  0
            352 CALL                     0
            362 POP_TOP
            364 LOAD_CONST               0 (None)
            366 RETURN_VALUE

Disassembly of <code object findtextchat at 0x777e474bd0, file "", line 334>:
              0 COPY_FREE_VARS           1

334           2 RESUME                   0

335           4 LOAD_DEREF               3 (browser)
              6 LOAD_METHOD              0 (open)
             28 LOAD_FAST                0 (curl)
             30 PRECALL                  1
             34 CALL                     1
             44 STORE_FAST               1 (r)

336          46 LOAD_DEREF               3 (browser)
             48 LOAD_METHOD              1 (title)
             70 PRECALL                  0
             74 CALL                     0
             84 STORE_FAST               2 (x)

337          86 LOAD_FAST                2 (x)
             88 LOAD_CONST               1 ('Review recent login')
             90 COMPARE_OP               2 (==)
             96 POP_JUMP_FORWARD_IF_FALSE    30 (to 158)

338          98 LOAD_GLOBAL              5 (NULL + print)
            110 LOAD_CONST               2 ('\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.')
            112 PRECALL                  1
            116 CALL                     1
            126 POP_TOP

339         128 LOAD_GLOBAL              7 (NULL + exit)
            140 LOAD_CONST               3 (1)
            142 PRECALL                  1
            146 CALL                     1
            156 POP_TOP

340     >>  158 LOAD_FAST                2 (x)
            160 LOAD_CONST               4 ('Login approval needed')
            162 COMPARE_OP               2 (==)
            168 POP_JUMP_FORWARD_IF_FALSE    30 (to 230)

341         170 LOAD_GLOBAL              5 (NULL + print)
            182 LOAD_CONST               5 ('\nYour account is stuck on verification\nPlease do it and then re run the program.')
            184 PRECALL                  1
            188 CALL                     1
            198 POP_TOP

342         200 LOAD_GLOBAL              7 (NULL + exit)
            212 LOAD_CONST               3 (1)
            214 PRECALL                  1
            218 CALL                     1
            228 POP_TOP

343     >>  230 LOAD_FAST                2 (x)
            232 LOAD_CONST               6 ('Epsilon')
            234 COMPARE_OP               2 (==)
            240 POP_JUMP_FORWARD_IF_FALSE    32 (to 306)

344         242 LOAD_GLOBAL              5 (NULL + print)
            254 LOAD_CONST               7 ('\nYour account got locked, recover it kindly and re run the script.')
            256 PRECALL                  1
            260 CALL                     1
            270 POP_TOP

345         272 LOAD_GLOBAL              7 (NULL + exit)
            284 LOAD_CONST               3 (1)
            286 PRECALL                  1
            290 CALL                     1
            300 POP_TOP
            302 LOAD_CONST               0 (None)
            304 RETURN_VALUE

343     >>  306 LOAD_CONST               0 (None)
            308 RETURN_VALUE

Disassembly of <code object sendtextconvo at 0x78ee6741b0, file "", line 347>:
              0 COPY_FREE_VARS           4

347           2 RESUME                   0

348           4 NOP

349           6 LOAD_DEREF               3 (browser)
              8 LOAD_METHOD              0 (select_form)
             30 LOAD_CONST               1 (1)
             32 KW_NAMES                 2
             34 PRECALL                  1
             38 CALL                     1
             48 POP_TOP
             50 JUMP_FORWARD            51 (to 154)
        >>   52 PUSH_EXC_INFO

350          54 LOAD_DEREF               6 (mechanize)
             56 LOAD_ATTR                1 (_mechanize)
             66 LOAD_ATTR                2 (FormNotFoundError)
             76 CHECK_EXC_MATCH
             78 POP_JUMP_FORWARD_IF_FALSE    33 (to 146)
             80 POP_TOP

351          82 LOAD_GLOBAL              7 (NULL + print)
             94 LOAD_CONST               3 ('Some error occured while finding text area, please check your account')
             96 PRECALL                  1
            100 CALL                     1
            110 POP_TOP

352         112 LOAD_GLOBAL              9 (NULL + exit)
            124 LOAD_CONST               1 (1)
            126 PRECALL                  1
            130 CALL                     1
            140 POP_TOP
            142 POP_EXCEPT
            144 JUMP_FORWARD             4 (to 154)

350     >>  146 RERAISE                  0
        >>  148 COPY                     3
            150 POP_EXCEPT
            152 RERAISE                  1

353     >>  154 NOP

354         156 LOAD_FAST                0 (comment)
            158 LOAD_DEREF               3 (browser)
            160 LOAD_ATTR                5 (form)
            170 LOAD_CONST               4 ('body')
            172 STORE_SUBSCR
            176 JUMP_FORWARD            51 (to 280)
        >>  178 PUSH_EXC_INFO

355         180 LOAD_DEREF               6 (mechanize)
            182 LOAD_ATTR                6 (_form_controls)
            192 LOAD_ATTR                7 (ControlNotFoundError)
            202 CHECK_EXC_MATCH
            204 POP_JUMP_FORWARD_IF_FALSE    33 (to 272)
            206 POP_TOP

356         208 LOAD_GLOBAL              7 (NULL + print)
            220 LOAD_CONST               5 ('Some error occured while filling text, please check your account')
            222 PRECALL                  1
            226 CALL                     1
            236 POP_TOP

357         238 LOAD_GLOBAL              9 (NULL + exit)
            250 LOAD_CONST               1 (1)
            252 PRECALL                  1
            256 CALL                     1
            266 POP_TOP
            268 POP_EXCEPT
            270 JUMP_FORWARD             4 (to 280)

355     >>  272 RERAISE                  0
        >>  274 COPY                     3
            276 POP_EXCEPT
            278 RERAISE                  1

358     >>  280 LOAD_DEREF               3 (browser)
            282 LOAD_METHOD              8 (submit)
            304 PRECALL                  0
            308 CALL                     0
            318 STORE_FAST               1 (r)

359         320 LOAD_DEREF               4 (datetime)
            322 LOAD_ATTR                9 (datetime)
            332 LOAD_METHOD             10 (now)
            354 PRECALL                  0
            358 CALL                     0
            368 STORE_FAST               2 (e)

360         370 LOAD_GLOBAL              7 (NULL + print)
            382 LOAD_CONST               6 ('\x1b[1;32m')
            384 LOAD_CONST               7 ('')
            386 KW_NAMES                 8
            388 PRECALL                  2
            392 CALL                     2
            402 POP_TOP

361         404 LOAD_GLOBAL              7 (NULL + print)
            416 LOAD_FAST                2 (e)
            418 LOAD_METHOD             11 (strftime)
            440 LOAD_CONST               9 ('\x1b[1;36mMESSEGE SEND SUCCESSFUL :Date - %d/%m/%Y Time - %I:%M:%S %p')
            442 PRECALL                  1
            446 CALL                     1
            456 PRECALL                  1
            460 CALL                     1
            470 POP_TOP

362         472 LOAD_GLOBAL              7 (NULL + print)
            484 LOAD_CONST              10 ('[•]\x1b[1;33mWELCOME TO M9HT9B T00L :: \x1b[1;32m')
            486 LOAD_DEREF               5 (line)
            488 LOAD_CONST              11 ('\n')
            490 PRECALL                  3
            494 CALL                     3
            504 POP_TOP
            506 LOAD_CONST               0 (None)
            508 RETURN_VALUE
ExceptionTable:
  6 to 48 -> 52 [0]
  52 to 140 -> 148 [1] lasti
  146 to 146 -> 148 [1] lasti
  156 to 174 -> 178 [0]
  178 to 266 -> 274 [1] lasti
  272 to 272 -> 274 [1] lasti

Disassembly of <code object m4 at 0x791e662a80, file "", line 419>:              0 MAKE_CELL               16 (PASSWORD)
              2 MAKE_CELL               17 (USERNAME)
              4 MAKE_CELL               18 (browser)
              6 MAKE_CELL               19 (datetime)
              8 MAKE_CELL               20 (line)
             10 MAKE_CELL               21 (mechanize)
             12 MAKE_CELL               22 (os)
             14 MAKE_CELL               23 (sleep)
             16 MAKE_CELL               24 (sp)
             18 MAKE_CELL               25 (sys)
             20 MAKE_CELL               26 (url)

419          22 RESUME                   0

421          24 LOAD_CONST               1 (0)
             26 LOAD_CONST               2 (('response',))
             28 IMPORT_NAME              0 (urllib)
             30 IMPORT_FROM              1 (response)
             32 STORE_FAST               0 (response)
             34 POP_TOP

422          36 LOAD_CONST               1 (0)
             38 LOAD_CONST               0 (None)
             40 IMPORT_NAME              2 (mechanize)
             42 STORE_DEREF             21 (mechanize)

423          44 LOAD_CONST               1 (0)
             46 LOAD_CONST               0 (None)
             48 IMPORT_NAME              3 (uuid)
             50 STORE_FAST               1 (uuid)

424          52 LOAD_CONST               1 (0)
             54 LOAD_CONST               0 (None)
             56 IMPORT_NAME              4 (os)
             58 STORE_DEREF             22 (os)

425          60 LOAD_CONST               1 (0)
             62 LOAD_CONST               0 (None)
             64 IMPORT_NAME              5 (datetime)
             66 STORE_DEREF             19 (datetime)

426          68 LOAD_CONST               1 (0)
             70 LOAD_CONST               0 (None)
             72 IMPORT_NAME              6 (time)
             74 STORE_FAST               2 (time)

427          76 LOAD_CONST               1 (0)
             78 LOAD_CONST               0 (None)
             80 IMPORT_NAME              7 (sys)
             82 STORE_DEREF             25 (sys)

428          84 LOAD_CONST               1 (0)
             86 LOAD_CONST               3 (('sleep',))
             88 IMPORT_NAME              6 (time)
             90 IMPORT_FROM              8 (sleep)
             92 STORE_DEREF             23 (sleep)
             94 POP_TOP

429          96 PUSH_NULL
             98 LOAD_DEREF              21 (mechanize)
            100 LOAD_ATTR                9 (Browser)
            110 PRECALL                  0
            114 CALL                     0
            124 STORE_DEREF             18 (browser)

430         126 LOAD_DEREF              18 (browser)
            128 LOAD_METHOD             10 (set_handle_robots)
            150 LOAD_CONST               4 (False)
            152 PRECALL                  1
            156 CALL                     1
            166 POP_TOP

431         168 PUSH_NULL
            170 LOAD_DEREF              21 (mechanize)
            172 LOAD_ATTR               11 (CookieJar)
            182 PRECALL                  0
            186 CALL                     0
            196 STORE_FAST               3 (cookies)

432         198 LOAD_DEREF              18 (browser)
            200 LOAD_METHOD             12 (set_cookiejar)
            222 LOAD_FAST                3 (cookies)
            224 PRECALL                  1
            228 CALL                     1
            238 POP_TOP

433         240 LOAD_CONST               5 (('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'))
            242 BUILD_LIST               1
            244 LOAD_DEREF              18 (browser)
            246 STORE_ATTR              13 (addheaders)

434         256 LOAD_DEREF              18 (browser)
            258 LOAD_METHOD             14 (set_handle_refresh)
            280 LOAD_CONST               4 (False)
            282 PRECALL                  1
            286 CALL                     1
            296 POP_TOP

438         298 LOAD_CONST               6 ('https://mbasic.facebook.com/login')
            300 STORE_DEREF             26 (url)

440         302 LOAD_CLOSURE            22 (os)
            304 BUILD_TUPLE              1
            306 LOAD_CONST               7 (<code object clear at 0x777e5b56b0, file "", line 440>)
            308 MAKE_FUNCTION            8 (closure)
            310 STORE_FAST               4 (clear)

447         312 LOAD_CLOSURE            23 (sleep)
            314 LOAD_CLOSURE            25 (sys)
            316 BUILD_TUPLE              2
            318 LOAD_CONST               8 (<code object sp at 0x777e5f5070, file "", line 447>)
            320 MAKE_FUNCTION            8 (closure)
            322 STORE_DEREF             24 (sp)

453         324 LOAD_CLOSURE            16 (PASSWORD)
            326 LOAD_CLOSURE            17 (USERNAME)
            328 LOAD_CLOSURE            18 (browser)
            330 LOAD_CLOSURE            21 (mechanize)
            332 LOAD_CLOSURE            24 (sp)
            334 LOAD_CLOSURE            26 (url)
            336 BUILD_TUPLE              6
            338 LOAD_CONST               9 (<code object login at 0x790e6708c0, file "", line 453>)
            340 MAKE_FUNCTION            8 (closure)
            342 STORE_FAST               5 (login)

489         344 LOAD_CLOSURE            18 (browser)
            346 BUILD_TUPLE              1
            348 LOAD_CONST              10 (<code object findtextchat at 0x777e474dc0, file "", line 489>)
            350 MAKE_FUNCTION            8 (closure)
            352 STORE_FAST               6 (findtextchat)

502         354 LOAD_CLOSURE            18 (browser)
            356 LOAD_CLOSURE            19 (datetime)
            358 LOAD_CLOSURE            20 (line)
            360 LOAD_CLOSURE            21 (mechanize)
            362 BUILD_TUPLE              4
            364 LOAD_CONST              11 (<code object sendtextconvo at 0x78ee675790, file "", line 502>)
            366 MAKE_FUNCTION            8 (closure)
            368 STORE_FAST               7 (sendtextconvo)

518         370 PUSH_NULL
            372 LOAD_DEREF              22 (os)
            374 LOAD_ATTR               15 (system)
            384 LOAD_CONST              12 ('clear')
            386 PRECALL                  1
            390 CALL                     1
            400 POP_TOP

519         402 LOAD_GLOBAL             33 (NULL + print)
            414 LOAD_CONST              13 ('\x1b[1;33;40m')
            416 LOAD_CONST              14 ('')
            418 KW_NAMES                15
            420 PRECALL                  2
            424 CALL                     2
            434 POP_TOP

520         436 LOAD_GLOBAL             33 (NULL + print)
            448 LOAD_GLOBAL             34 (logo)
            460 PRECALL                  1
            464 CALL                     1
            474 POP_TOP

521         476 LOAD_GLOBAL             33 (NULL + print)
            488 LOAD_CONST              16 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
            490 PRECALL                  1
            494 CALL                     1
            504 POP_TOP

522         506 LOAD_GLOBAL             33 (NULL + print)
            518 LOAD_CONST              17 ('-----------------------------------------------')
            520 PRECALL                  1
            524 CALL                     1
            534 POP_TOP

523         536 PUSH_NULL
            538 LOAD_DEREF              24 (sp)
            540 LOAD_CONST              18 ('\x1b[1;32m[+] \x1b[1;32mLOGIN FB ID TYP NUMBER & GMAIL AND PASWAD\n')
            542 PRECALL                  1
            546 CALL                     1
            556 POP_TOP

524         558 LOAD_GLOBAL             33 (NULL + print)
            570 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
            572 PRECALL                  1
            576 CALL                     1
            586 POP_TOP

525         588 LOAD_GLOBAL             37 (NULL + str)
            600 LOAD_GLOBAL             39 (NULL + input)
            612 LOAD_CONST              20 ('\x1b[1;32m[+] TYPE NUMBER & GAMIL : ')
            614 PRECALL                  1
            618 CALL                     1
            628 PRECALL                  1
            632 CALL                     1
            642 STORE_DEREF             17 (USERNAME)

526         644 LOAD_GLOBAL             33 (NULL + print)
            656 LOAD_CONST              13 ('\x1b[1;33;40m')
            658 LOAD_CONST              14 ('')
            660 KW_NAMES                15
            662 PRECALL                  2
            666 CALL                     2
            676 POP_TOP

527         678 LOAD_GLOBAL             33 (NULL + print)
            690 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
            692 PRECALL                  1
            696 CALL                     1
            706 POP_TOP

528         708 LOAD_GLOBAL             37 (NULL + str)
            720 LOAD_GLOBAL             39 (NULL + input)
            732 LOAD_CONST              21 ('\x1b[1;32m[?] TYP3 PASWAD: ')
            734 PRECALL                  1
            738 CALL                     1
            748 PRECALL                  1
            752 CALL                     1
            762 STORE_DEREF             16 (PASSWORD)

529         764 PUSH_NULL
            766 LOAD_FAST                5 (login)
            768 PRECALL                  0
            772 CALL                     0
            782 POP_TOP

530         784 LOAD_GLOBAL             33 (NULL + print)
            796 LOAD_CONST              22 ('\x1b[1;34;40m')
            798 LOAD_CONST              14 ('')
            800 KW_NAMES                15
            802 PRECALL                  2
            806 CALL                     2
            816 POP_TOP

531         818 PUSH_NULL
            820 LOAD_DEREF              22 (os)
            822 LOAD_ATTR               15 (system)
            832 LOAD_CONST              12 ('clear')
            834 PRECALL                  1
            838 CALL                     1
            848 POP_TOP

532         850 LOAD_GLOBAL             33 (NULL + print)
            862 LOAD_GLOBAL             34 (logo)
            874 PRECALL                  1
            878 CALL                     1
            888 POP_TOP

533         890 LOAD_GLOBAL             33 (NULL + print)
            902 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
            904 PRECALL                  1
            908 CALL                     1
            918 POP_TOP

534         920 LOAD_GLOBAL             37 (NULL + str)
            932 LOAD_GLOBAL             39 (NULL + input)
            944 LOAD_CONST              23 ('\x1b[1;32m[?] \x1b[1;32mENTER CHET INBOX LINK : ')
            946 PRECALL                  1
            950 CALL                     1
            960 PRECALL                  1
            964 CALL                     1
            974 STORE_FAST               8 (cid)

535         976 LOAD_CONST              24 ('https://mbasic.facebook.com/messages/t/')
            978 LOAD_GLOBAL             37 (NULL + str)
            990 LOAD_FAST                8 (cid)
            992 PRECALL                  1
            996 CALL                     1
           1006 BINARY_OP                0 (+)
           1010 STORE_FAST               9 (curl)

537        1012 LOAD_GLOBAL             33 (NULL + print)
           1024 LOAD_CONST              22 ('\x1b[1;34;40m')
           1026 LOAD_CONST              14 ('')
           1028 KW_NAMES                15
           1030 PRECALL                  2
           1034 CALL                     2
           1044 POP_TOP

538        1046 LOAD_GLOBAL             33 (NULL + print)
           1058 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1060 PRECALL                  1
           1064 CALL                     1
           1074 POP_TOP

539        1076 LOAD_GLOBAL             37 (NULL + str)
           1088 LOAD_GLOBAL             39 (NULL + input)
           1100 LOAD_CONST              25 ('\x1b[1;32m[?] \x1b[1;32mEnter File Name : ')
           1102 PRECALL                  1
           1106 CALL                     1
           1116 PRECALL                  1
           1120 CALL                     1
           1130 STORE_FAST              10 (np)

540        1132 LOAD_GLOBAL             41 (NULL + open)
           1144 LOAD_FAST               10 (np)
           1146 LOAD_CONST              26 ('r')
           1148 PRECALL                  2
           1152 CALL                     2
           1162 STORE_FAST              11 (f)

541        1164 LOAD_FAST               11 (f)
           1166 LOAD_METHOD             21 (readlines)
           1188 PRECALL                  0
           1192 CALL                     0
           1202 STORE_FAST              12 (lines)

542        1204 LOAD_FAST               11 (f)
           1206 LOAD_METHOD             22 (close)
           1228 PRECALL                  0
           1232 CALL                     0
           1242 POP_TOP

543        1244 LOAD_GLOBAL             33 (NULL + print)
           1256 LOAD_CONST              13 ('\x1b[1;33;40m')
           1258 LOAD_CONST              14 ('')
           1260 KW_NAMES                15
           1262 PRECALL                  2
           1266 CALL                     2
           1276 POP_TOP

544        1278 LOAD_GLOBAL             33 (NULL + print)
           1290 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1292 PRECALL                  1
           1296 CALL                     1
           1306 POP_TOP

545        1308 PUSH_NULL
           1310 LOAD_DEREF              24 (sp)
           1312 LOAD_CONST              27 ('\x1b[1;32m[?] \x1b[1;32mEnter The Time Delay In Seconds\n')
           1314 PRECALL                  1
           1318 CALL                     1
           1328 POP_TOP

546        1330 LOAD_GLOBAL             33 (NULL + print)
           1342 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1344 PRECALL                  1
           1348 CALL                     1
           1358 POP_TOP

547        1360 LOAD_GLOBAL             47 (NULL + int)
           1372 LOAD_GLOBAL             39 (NULL + input)
           1384 LOAD_CONST              28 ('\x1b[1;32m[?] \x1b[1;32mEnter Time : ')
           1386 PRECALL                  1
           1390 CALL                     1
           1400 PRECALL                  1
           1404 CALL                     1
           1414 STORE_FAST              13 (t)

549        1416 PUSH_NULL
           1418 LOAD_DEREF              22 (os)
           1420 LOAD_ATTR               15 (system)
           1430 LOAD_CONST              12 ('clear')
           1432 PRECALL                  1
           1436 CALL                     1
           1446 POP_TOP

550        1448 LOAD_GLOBAL             33 (NULL + print)
           1460 LOAD_GLOBAL             34 (logo)
           1472 PRECALL                  1
           1476 CALL                     1
           1486 POP_TOP

551        1488 LOAD_GLOBAL             33 (NULL + print)
           1500 LOAD_CONST              16 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
           1502 PRECALL                  1
           1506 CALL                     1
           1516 POP_TOP

552        1518 LOAD_GLOBAL             33 (NULL + print)
           1530 LOAD_CONST              19 ('\x1b[1;37m-----------------------------------------------')
           1532 PRECALL                  1
           1536 CALL                     1
           1546 POP_TOP

553        1548 LOAD_CONST               1 (0)
           1550 STORE_FAST              14 (count)

554        1552 NOP

555     >> 1554 NOP

556        1556 LOAD_FAST               12 (lines)
           1558 GET_ITER
        >> 1560 FOR_ITER               110 (to 1782)
           1562 STORE_DEREF             20 (line)

557        1564 LOAD_GLOBAL             49 (NULL + len)
           1576 LOAD_DEREF              20 (line)
           1578 PRECALL                  1
           1582 CALL                     1
           1592 LOAD_CONST              30 (3)
           1594 COMPARE_OP               4 (>)
           1600 POP_JUMP_FORWARD_IF_FALSE    89 (to 1780)

558        1602 LOAD_FAST               14 (count)
           1604 LOAD_CONST               1 (0)
           1606 COMPARE_OP               3 (!=)
           1612 POP_JUMP_FORWARD_IF_FALSE    11 (to 1636)

559        1614 PUSH_NULL
           1616 LOAD_DEREF              23 (sleep)
           1618 LOAD_FAST               13 (t)
           1620 PRECALL                  1
           1624 CALL                     1
           1634 POP_TOP

560     >> 1636 PUSH_NULL
           1638 LOAD_FAST                6 (findtextchat)
           1640 LOAD_FAST                9 (curl)
           1642 PRECALL                  1
           1646 CALL                     1
           1656 POP_TOP

561        1658 PUSH_NULL
           1660 LOAD_FAST                7 (sendtextconvo)
           1662 LOAD_DEREF              20 (line)
           1664 PRECALL                  1
           1668 CALL                     1
           1678 POP_TOP

562        1680 LOAD_FAST               14 (count)
           1682 LOAD_CONST              31 (1)
           1684 BINARY_OP               13 (+=)
           1688 STORE_FAST              14 (count)

563        1690 LOAD_FAST               14 (count)
           1692 LOAD_CONST              32 (10)
           1694 BINARY_OP                6 (%)
           1698 LOAD_CONST               1 (0)
           1700 COMPARE_OP               2 (==)
           1706 POP_JUMP_FORWARD_IF_FALSE    36 (to 1780)

564        1708 PUSH_NULL
           1710 LOAD_DEREF              23 (sleep)
           1712 LOAD_CONST              31 (1)
           1714 PRECALL                  1
           1718 CALL                     1
           1728 POP_TOP

565        1730 PUSH_NULL
           1732 LOAD_FAST                4 (clear)
           1734 PRECALL                  0
           1738 CALL                     0
           1748 POP_TOP

566        1750 LOAD_GLOBAL             33 (NULL + print)
           1762 LOAD_CONST              33 ('\x1b[1;32m')
           1764 PRECALL                  1
           1768 CALL                     1
           1778 POP_TOP
        >> 1780 JUMP_BACKWARD          111 (to 1560)

556     >> 1782 JUMP_FORWARD            49 (to 1882)
        >> 1784 PUSH_EXC_INFO

567        1786 LOAD_GLOBAL             50 (Exception)
           1798 CHECK_EXC_MATCH
           1800 POP_JUMP_FORWARD_IF_FALSE    36 (to 1874)
           1802 STORE_FAST              15 (e)

568        1804 LOAD_GLOBAL             33 (NULL + print)
           1816 LOAD_FAST               15 (e)
           1818 PRECALL                  1
           1822 CALL                     1
           1832 POP_TOP

569        1834 PUSH_NULL
           1836 LOAD_DEREF              23 (sleep)
           1838 LOAD_CONST              30 (3)
           1840 PRECALL                  1
           1844 CALL                     1
           1854 POP_TOP
           1856 POP_EXCEPT
           1858 LOAD_CONST               0 (None)
           1860 STORE_FAST              15 (e)
           1862 DELETE_FAST             15 (e)
           1864 JUMP_FORWARD             8 (to 1882)
        >> 1866 LOAD_CONST               0 (None)
           1868 STORE_FAST              15 (e)
           1870 DELETE_FAST             15 (e)
           1872 RERAISE                  1

567     >> 1874 RERAISE                  0
        >> 1876 COPY                     3
           1878 POP_EXCEPT
           1880 RERAISE                  1

554     >> 1882 JUMP_BACKWARD          165 (to 1554)
ExceptionTable:
  1556 to 1780 -> 1784 [0]
  1784 to 1802 -> 1876 [1] lasti
  1804 to 1854 -> 1866 [1] lasti
  1866 to 1874 -> 1876 [1] lasti

Disassembly of <code object clear at 0x777e5b56b0, file "", line 440>:
              0 COPY_FREE_VARS           1

440           2 RESUME                   0

441           4 LOAD_DEREF               0 (os)
              6 LOAD_ATTR                0 (name)
             16 LOAD_CONST               1 ('nt')
             18 COMPARE_OP               2 (==)
             24 POP_JUMP_FORWARD_IF_FALSE    18 (to 62)

442          26 PUSH_NULL
             28 LOAD_DEREF               0 (os)
             30 LOAD_ATTR                1 (system)
             40 LOAD_CONST               2 ('cls')
             42 PRECALL                  1
             46 CALL                     1
             56 POP_TOP
             58 LOAD_CONST               0 (None)
             60 RETURN_VALUE

444     >>   62 PUSH_NULL
             64 LOAD_DEREF               0 (os)
             66 LOAD_ATTR                1 (system)
             76 LOAD_CONST               3 ('xdg-open ')
             78 PRECALL                  1
             82 CALL                     1
             92 POP_TOP
             94 LOAD_CONST               0 (None)
             96 RETURN_VALUE

Disassembly of <code object sp at 0x777e5f5070, file "", line 447>:              0 COPY_FREE_VARS           2

447           2 RESUME                   0

448           4 LOAD_FAST                0 (stri)
              6 GET_ITER
        >>    8 FOR_ITER                55 (to 120)
             10 STORE_FAST               1 (letter)

449          12 LOAD_GLOBAL              1 (NULL + print)
             24 LOAD_FAST                1 (letter)
             26 LOAD_CONST               1 ('')
             28 KW_NAMES                 2
             30 PRECALL                  2
             34 CALL                     2
             44 POP_TOP

450          46 LOAD_DEREF               3 (sys)
             48 LOAD_ATTR                1 (stdout)
             58 LOAD_METHOD              2 (flush)
             80 PRECALL                  0
             84 CALL                     0
             94 POP_TOP

451          96 PUSH_NULL
             98 LOAD_DEREF               2 (sleep)
            100 LOAD_CONST               3 (0.03)
            102 PRECALL                  1
            106 CALL                     1
            116 POP_TOP
            118 JUMP_BACKWARD           56 (to 8)

448     >>  120 LOAD_CONST               0 (None)
            122 RETURN_VALUE

Disassembly of <code object login at 0x790e6708c0, file "", line 453>:
              0 COPY_FREE_VARS           6

453           2 RESUME                   0

454           4 LOAD_DEREF               5 (browser)
              6 LOAD_METHOD              0 (open)
             28 LOAD_DEREF               8 (url)
             30 PRECALL                  1
             34 CALL                     1
             44 POP_TOP

455          46 LOAD_DEREF               5 (browser)
             48 LOAD_METHOD              1 (select_form)
             70 LOAD_CONST               1 (0)
             72 KW_NAMES                 2
             74 PRECALL                  1
             78 CALL                     1
             88 POP_TOP

456          90 LOAD_DEREF               4 (USERNAME)
             92 LOAD_DEREF               5 (browser)
             94 LOAD_ATTR                2 (form)
            104 LOAD_CONST               3 ('email')
            106 STORE_SUBSCR

457         110 LOAD_DEREF               3 (PASSWORD)
            112 LOAD_DEREF               5 (browser)
            114 LOAD_ATTR                2 (form)
            124 LOAD_CONST               4 ('pass')
            126 STORE_SUBSCR

458         130 LOAD_DEREF               5 (browser)
            132 LOAD_METHOD              3 (submit)
            154 PRECALL                  0
            158 CALL                     0
            168 STORE_FAST               0 (r)

459         170 LOAD_GLOBAL              1 (NULL + open)
            182 LOAD_CONST               5 ('login.html')
            184 LOAD_CONST               6 ('wb')
            186 PRECALL                  2
            190 CALL                     2
            200 STORE_FAST               1 (f)

460         202 LOAD_FAST                1 (f)
            204 LOAD_METHOD              4 (write)
            226 LOAD_FAST                0 (r)
            228 LOAD_METHOD              5 (read)
            250 PRECALL                  0
            254 CALL                     0
            264 PRECALL                  1
            268 CALL                     1
            278 POP_TOP

461         280 LOAD_DEREF               5 (browser)
            282 LOAD_METHOD              1 (select_form)
            304 LOAD_CONST               1 (0)
            306 KW_NAMES                 2
            308 PRECALL                  1
            312 CALL                     1
            322 POP_TOP

462         324 LOAD_GLOBAL             13 (NULL + print)
            336 LOAD_CONST               7 ('\x1b[1m\x1b[36m')
            338 LOAD_CONST               8 ('')
            340 KW_NAMES                 9
            342 PRECALL                  2
            346 CALL                     2
            356 POP_TOP

463         358 LOAD_GLOBAL             13 (NULL + print)
            370 LOAD_CONST              10 ('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
            372 PRECALL                  1
            376 CALL                     1
            386 POP_TOP

464         388 PUSH_NULL
            390 LOAD_DEREF               7 (sp)
            392 LOAD_CONST              11 ('\x1b[1;37;1m[?] Enter the 2 factor code by google authenticator\n')
            394 PRECALL                  1
            398 CALL                     1
            408 POP_TOP

465         410 LOAD_GLOBAL             13 (NULL + print)
            422 LOAD_CONST              12 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            424 PRECALL                  1
            428 CALL                     1
            438 POP_TOP

466         440 LOAD_GLOBAL             15 (NULL + str)
            452 LOAD_GLOBAL             17 (NULL + input)
            464 LOAD_CONST              13 ('\x1b[1;37;1m[?] Enter Code : ')
            466 PRECALL                  1
            470 CALL                     1
            480 PRECALL                  1
            484 CALL                     1
            494 STORE_FAST               2 (apr)

467         496 NOP

468         498 LOAD_FAST                2 (apr)
            500 LOAD_DEREF               5 (browser)
            502 LOAD_ATTR                2 (form)
            512 LOAD_CONST              14 ('approvals_code')
            514 STORE_SUBSCR
            518 JUMP_FORWARD           145 (to 810)
        >>  520 PUSH_EXC_INFO

469         522 LOAD_DEREF               6 (mechanize)
            524 LOAD_ATTR                9 (_form_controls)
            534 LOAD_ATTR               10 (ControlNotFoundError)
            544 CHECK_EXC_MATCH
            546 POP_JUMP_FORWARD_IF_FALSE   127 (to 802)
            548 POP_TOP

470         550 LOAD_GLOBAL             13 (NULL + print)
            562 LOAD_CONST              15 ('Wrong password or some shit, check generated file')
            564 PRECALL                  1
            568 CALL                     1
            578 POP_TOP

471         580 LOAD_GLOBAL              1 (NULL + open)
            592 LOAD_CONST              16 ('epage_')
            594 LOAD_GLOBAL             15 (NULL + str)
            606 LOAD_DEREF               4 (USERNAME)
            608 PRECALL                  1
            612 CALL                     1
            622 BINARY_OP                0 (+)
            626 LOAD_CONST              17 ('.html')
            628 BINARY_OP                0 (+)
            632 LOAD_CONST               6 ('wb')
            634 PRECALL                  2
            638 CALL                     2
            648 STORE_FAST               1 (f)

472         650 LOAD_FAST                1 (f)
            652 LOAD_METHOD              4 (write)
            674 LOAD_FAST                0 (r)
            676 LOAD_METHOD              5 (read)
            698 PRECALL                  0
            702 CALL                     0
            712 PRECALL                  1
            716 CALL                     1
            726 POP_TOP

473         728 LOAD_FAST                1 (f)
            730 LOAD_METHOD             11 (close)
            752 PRECALL                  0
            756 CALL                     0
            766 POP_TOP

474         768 LOAD_GLOBAL             25 (NULL + exit)
            780 LOAD_CONST              18 (1)
            782 PRECALL                  1
            786 CALL                     1
            796 POP_TOP
            798 POP_EXCEPT
            800 JUMP_FORWARD             4 (to 810)

469     >>  802 RERAISE                  0
        >>  804 COPY                     3
            806 POP_EXCEPT
            808 RERAISE                  1

475     >>  810 LOAD_DEREF               5 (browser)
            812 LOAD_METHOD              3 (submit)
            834 PRECALL                  0
            838 CALL                     0
            848 STORE_FAST               0 (r)

476         850 LOAD_DEREF               5 (browser)
            852 LOAD_METHOD              1 (select_form)
            874 LOAD_CONST               1 (0)
            876 KW_NAMES                 2
            878 PRECALL                  1
            882 CALL                     1
            892 POP_TOP

477         894 NOP

478         896 LOAD_CONST              19 ('save_device')
            898 BUILD_LIST               1
            900 LOAD_DEREF               5 (browser)
            902 LOAD_ATTR                2 (form)
            912 LOAD_CONST              20 ('name_action_selected')            914 STORE_SUBSCR
            918 JUMP_FORWARD           145 (to 1210)
        >>  920 PUSH_EXC_INFO

479         922 LOAD_DEREF               6 (mechanize)
            924 LOAD_ATTR                9 (_form_controls)
            934 LOAD_ATTR               10 (ControlNotFoundError)
            944 CHECK_EXC_MATCH
            946 POP_JUMP_FORWARD_IF_FALSE   127 (to 1202)
            948 POP_TOP

480         950 LOAD_GLOBAL             13 (NULL + print)
            962 LOAD_CONST              21 ('Some shit gone down, check generated file')
            964 PRECALL                  1
            968 CALL                     1
            978 POP_TOP

481         980 LOAD_GLOBAL              1 (NULL + open)
            992 LOAD_CONST              16 ('epage_')
            994 LOAD_GLOBAL             15 (NULL + str)
           1006 LOAD_DEREF               4 (USERNAME)
           1008 PRECALL                  1
           1012 CALL                     1
           1022 BINARY_OP                0 (+)
           1026 LOAD_CONST              17 ('.html')
           1028 BINARY_OP                0 (+)
           1032 LOAD_CONST               6 ('wb')
           1034 PRECALL                  2
           1038 CALL                     2
           1048 STORE_FAST               1 (f)

482        1050 LOAD_FAST                1 (f)
           1052 LOAD_METHOD              4 (write)
           1074 LOAD_FAST                0 (r)
           1076 LOAD_METHOD              5 (read)
           1098 PRECALL                  0
           1102 CALL                     0
           1112 PRECALL                  1
           1116 CALL                     1
           1126 POP_TOP

483        1128 LOAD_FAST                1 (f)
           1130 LOAD_METHOD             11 (close)
           1152 PRECALL                  0
           1156 CALL                     0
           1166 POP_TOP

484        1168 LOAD_GLOBAL             25 (NULL + exit)
           1180 LOAD_CONST              18 (1)
           1182 PRECALL                  1
           1186 CALL                     1
           1196 POP_TOP
           1198 POP_EXCEPT
           1200 JUMP_FORWARD             4 (to 1210)

479     >> 1202 RERAISE                  0
        >> 1204 COPY                     3
           1206 POP_EXCEPT
           1208 RERAISE                  1

485     >> 1210 LOAD_DEREF               5 (browser)
           1212 LOAD_METHOD              3 (submit)
           1234 PRECALL                  0
           1238 CALL                     0
           1248 STORE_FAST               0 (r)

486        1250 LOAD_GLOBAL              1 (NULL + open)
           1262 LOAD_CONST              22 ('full_login_')
           1264 LOAD_GLOBAL             15 (NULL + str)
           1276 LOAD_DEREF               4 (USERNAME)
           1278 PRECALL                  1
           1282 CALL                     1
           1292 BINARY_OP                0 (+)
           1296 LOAD_CONST              17 ('.html')
           1298 BINARY_OP                0 (+)
           1302 LOAD_CONST               6 ('wb')
           1304 PRECALL                  2
           1308 CALL                     2
           1318 STORE_FAST               1 (f)

487        1320 LOAD_FAST                1 (f)
           1322 LOAD_METHOD              4 (write)
           1344 LOAD_FAST                0 (r)
           1346 LOAD_METHOD              5 (read)
           1368 PRECALL                  0
           1372 CALL                     0
           1382 PRECALL                  1
           1386 CALL                     1
           1396 POP_TOP

488        1398 LOAD_FAST                1 (f)
           1400 LOAD_METHOD             11 (close)
           1422 PRECALL                  0
           1426 CALL                     0
           1436 POP_TOP
           1438 LOAD_CONST               0 (None)
           1440 RETURN_VALUE
ExceptionTable:
  498 to 516 -> 520 [0]
  520 to 796 -> 804 [1] lasti
  802 to 802 -> 804 [1] lasti
  896 to 916 -> 920 [0]
  920 to 1196 -> 1204 [1] lasti
  1202 to 1202 -> 1204 [1] lasti

Disassembly of <code object findtextchat at 0x777e474dc0, file "", line 489>:
              0 COPY_FREE_VARS           1

489           2 RESUME                   0

490           4 LOAD_DEREF               3 (browser)
              6 LOAD_METHOD              0 (open)
             28 LOAD_FAST                0 (curl)
             30 PRECALL                  1
             34 CALL                     1
             44 STORE_FAST               1 (r)

491          46 LOAD_DEREF               3 (browser)
             48 LOAD_METHOD              1 (title)
             70 PRECALL                  0
             74 CALL                     0
             84 STORE_FAST               2 (x)

492          86 LOAD_FAST                2 (x)
             88 LOAD_CONST               1 ('Review recent login')
             90 COMPARE_OP               2 (==)
             96 POP_JUMP_FORWARD_IF_FALSE    30 (to 158)

493          98 LOAD_GLOBAL              5 (NULL + print)
            110 LOAD_CONST               2 ('\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.')
            112 PRECALL                  1
            116 CALL                     1
            126 POP_TOP

494         128 LOAD_GLOBAL              7 (NULL + exit)
            140 LOAD_CONST               3 (1)
            142 PRECALL                  1
            146 CALL                     1
            156 POP_TOP

495     >>  158 LOAD_FAST                2 (x)
            160 LOAD_CONST               4 ('Login approval needed')
            162 COMPARE_OP               2 (==)
            168 POP_JUMP_FORWARD_IF_FALSE    30 (to 230)

496         170 LOAD_GLOBAL              5 (NULL + print)
            182 LOAD_CONST               5 ('\nYour account is stuck on verification\nPlease do it and then re run the program.')
            184 PRECALL                  1
            188 CALL                     1
            198 POP_TOP

497         200 LOAD_GLOBAL              7 (NULL + exit)
            212 LOAD_CONST               3 (1)
            214 PRECALL                  1
            218 CALL                     1
            228 POP_TOP

498     >>  230 LOAD_FAST                2 (x)
            232 LOAD_CONST               6 ('Epsilon')
            234 COMPARE_OP               2 (==)
            240 POP_JUMP_FORWARD_IF_FALSE    32 (to 306)

499         242 LOAD_GLOBAL              5 (NULL + print)
            254 LOAD_CONST               7 ('\nYour account got locked, recover it kindly and re run the script.')
            256 PRECALL                  1
            260 CALL                     1
            270 POP_TOP

500         272 LOAD_GLOBAL              7 (NULL + exit)
            284 LOAD_CONST               3 (1)
            286 PRECALL                  1
            290 CALL                     1
            300 POP_TOP
            302 LOAD_CONST               0 (None)
            304 RETURN_VALUE

498     >>  306 LOAD_CONST               0 (None)
            308 RETURN_VALUE

Disassembly of <code object sendtextconvo at 0x78ee675790, file "", line 502>:
              0 COPY_FREE_VARS           4

502           2 RESUME                   0

503           4 NOP

504           6 LOAD_DEREF               3 (browser)
              8 LOAD_METHOD              0 (select_form)
             30 LOAD_CONST               1 (1)
             32 KW_NAMES                 2
             34 PRECALL                  1
             38 CALL                     1
             48 POP_TOP
             50 JUMP_FORWARD            51 (to 154)
        >>   52 PUSH_EXC_INFO

505          54 LOAD_DEREF               6 (mechanize)
             56 LOAD_ATTR                1 (_mechanize)
             66 LOAD_ATTR                2 (FormNotFoundError)
             76 CHECK_EXC_MATCH
             78 POP_JUMP_FORWARD_IF_FALSE    33 (to 146)
             80 POP_TOP

506          82 LOAD_GLOBAL              7 (NULL + print)
             94 LOAD_CONST               3 ('Some error occured while finding text area, please check your account')
             96 PRECALL                  1
            100 CALL                     1
            110 POP_TOP

507         112 LOAD_GLOBAL              9 (NULL + exit)
            124 LOAD_CONST               1 (1)
            126 PRECALL                  1
            130 CALL                     1
            140 POP_TOP
            142 POP_EXCEPT
            144 JUMP_FORWARD             4 (to 154)

505     >>  146 RERAISE                  0
        >>  148 COPY                     3
            150 POP_EXCEPT
            152 RERAISE                  1

508     >>  154 NOP

509         156 LOAD_FAST                0 (comment)
            158 LOAD_DEREF               3 (browser)
            160 LOAD_ATTR                5 (form)
            170 LOAD_CONST               4 ('body')
            172 STORE_SUBSCR
            176 JUMP_FORWARD            51 (to 280)
        >>  178 PUSH_EXC_INFO

510         180 LOAD_DEREF               6 (mechanize)
            182 LOAD_ATTR                6 (_form_controls)
            192 LOAD_ATTR                7 (ControlNotFoundError)
            202 CHECK_EXC_MATCH
            204 POP_JUMP_FORWARD_IF_FALSE    33 (to 272)
            206 POP_TOP

511         208 LOAD_GLOBAL              7 (NULL + print)
            220 LOAD_CONST               5 ('Some error occured while filling text, please check your account')
            222 PRECALL                  1
            226 CALL                     1
            236 POP_TOP

512         238 LOAD_GLOBAL              9 (NULL + exit)
            250 LOAD_CONST               1 (1)
            252 PRECALL                  1
            256 CALL                     1
            266 POP_TOP
            268 POP_EXCEPT
            270 JUMP_FORWARD             4 (to 280)

510     >>  272 RERAISE                  0
        >>  274 COPY                     3
            276 POP_EXCEPT
            278 RERAISE                  1

513     >>  280 LOAD_DEREF               3 (browser)
            282 LOAD_METHOD              8 (submit)
            304 PRECALL                  0
            308 CALL                     0
            318 STORE_FAST               1 (r)

514         320 LOAD_DEREF               4 (datetime)
            322 LOAD_ATTR                9 (datetime)
            332 LOAD_METHOD             10 (now)
            354 PRECALL                  0
            358 CALL                     0
            368 STORE_FAST               2 (e)

515         370 LOAD_GLOBAL              7 (NULL + print)
            382 LOAD_CONST               6 ('\x1b[1;32m')
            384 LOAD_CONST               7 ('')
            386 KW_NAMES                 8
            388 PRECALL                  2
            392 CALL                     2
            402 POP_TOP

516         404 LOAD_GLOBAL              7 (NULL + print)
            416 LOAD_FAST                2 (e)
            418 LOAD_METHOD             11 (strftime)
            440 LOAD_CONST               9 ('\x1b[1;36mMESSEGE SEND SUCCESSFUL :Date - %d/%m/%Y Time - %I:%M:%S %p')
            442 PRECALL                  1
            446 CALL                     1
            456 PRECALL                  1
            460 CALL                     1
            470 POP_TOP

517         472 LOAD_GLOBAL              7 (NULL + print)
            484 LOAD_CONST              10 ('[•]\x1b[1;33mWELCOME TO M9HT9B T00L :: \x1b[1;32m')
            486 LOAD_DEREF               5 (line)
            488 LOAD_CONST              11 ('\n')
            490 PRECALL                  3
            494 CALL                     3
            504 POP_TOP
            506 LOAD_CONST               0 (None)
            508 RETURN_VALUE
ExceptionTable:
  6 to 48 -> 52 [0]
  52 to 140 -> 148 [1] lasti
  146 to 146 -> 148 [1] lasti
  156 to 174 -> 178 [0]
  178 to 266 -> 274 [1] lasti
  272 to 272 -> 274 [1] lasti

Disassembly of <code object m2 at 0x790e66c860, file "", line 573>:              0 MAKE_CELL                9 (RequestException)
              2 MAKE_CELL               10 (access_token)
              4 MAKE_CELL               11 (cuid)
              6 MAKE_CELL               12 (headers)
              8 MAKE_CELL               13 (lines)
             10 MAKE_CELL               14 (os)
             12 MAKE_CELL               15 (requests)
             14 MAKE_CELL               16 (t)
             16 MAKE_CELL               17 (time)

573          18 RESUME                   0

575          20 LOAD_CONST               1 (0)
             22 LOAD_CONST               0 (None)
             24 IMPORT_NAME              0 (requests)
             26 STORE_DEREF             15 (requests)
             28 LOAD_CONST               1 (0)
             30 LOAD_CONST               0 (None)
             32 IMPORT_NAME              1 (os)
             34 STORE_DEREF             14 (os)
             36 LOAD_CONST               1 (0)
             38 LOAD_CONST               0 (None)
             40 IMPORT_NAME              2 (re)
             42 STORE_FAST               0 (re)
             44 LOAD_CONST               1 (0)
             46 LOAD_CONST               0 (None)
             48 IMPORT_NAME              3 (time)
             50 STORE_DEREF             17 (time)
             52 LOAD_CONST               1 (0)
             54 LOAD_CONST               0 (None)
             56 IMPORT_NAME              4 (random)
             58 STORE_FAST               1 (random)

576          60 LOAD_CONST               1 (0)
             62 LOAD_CONST               2 (('RequestException',))
             64 IMPORT_NAME              5 (requests.exceptions)
             66 IMPORT_FROM              6 (RequestException)
             68 STORE_DEREF              9 (RequestException)
             70 POP_TOP

577          72 LOAD_CONST               1 (0)
             74 LOAD_CONST               3 (('sleep',))
             76 IMPORT_NAME              3 (time)
             78 IMPORT_FROM              7 (sleep)
             80 STORE_FAST               2 (sleep)
             82 POP_TOP

578          84 LOAD_CONST               1 (0)
             86 LOAD_CONST               0 (None)
             88 IMPORT_NAME              8 (datetime)
             90 STORE_FAST               3 (datetime)

579          92 LOAD_CONST               1 (0)
             94 LOAD_CONST               0 (None)
             96 IMPORT_NAME              1 (os)
             98 STORE_DEREF             14 (os)

582         100 LOAD_CONST               4 ('keep-alive')

583         102 LOAD_CONST               5 ('max-age=0')

584         104 LOAD_CONST               6 ('1')

585         106 LOAD_CONST               7 ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')

586         108 LOAD_CONST               8 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')

587         110 LOAD_CONST               9 ('gzip, deflate')

588         112 LOAD_CONST              10 ('en-US,en;q=0.9,fr;q=0.8')

589         114 LOAD_CONST              11 ('www.google.com')

581         116 LOAD_CONST              12 (('Connection', 'Cache-Control', 'Upgrade-Insecure-Requests', 'User-Agent', 'Accept', 'Accept-Encoding', 'Accept-Language', 'referer'))
            118 BUILD_CONST_KEY_MAP      8
            120 STORE_DEREF             12 (headers)

592         122 LOAD_CLOSURE            14 (os)
            124 BUILD_TUPLE              1
            126 LOAD_CONST              13 (<code object clear at 0x777e5b57d0, file "", line 592>)
            128 MAKE_FUNCTION            8 (closure)
            130 STORE_FAST               4 (clear)

598         132 PUSH_NULL
            134 LOAD_FAST                4 (clear)
            136 PRECALL                  0
            140 CALL                     0
            150 POP_TOP

600         152 LOAD_CLOSURE             9 (RequestException)
            154 LOAD_CLOSURE            10 (access_token)
            156 LOAD_CLOSURE            11 (cuid)
            158 LOAD_CLOSURE            12 (headers)
            160 LOAD_CLOSURE            13 (lines)
            162 LOAD_CLOSURE            15 (requests)
            164 LOAD_CLOSURE            16 (t)
            166 LOAD_CLOSURE            17 (time)
            168 BUILD_TUPLE              8
            170 LOAD_CONST              14 (<code object sendcomment at 0x777e490940, file "", line 600>)
            172 MAKE_FUNCTION            8 (closure)
            174 STORE_FAST               5 (sendcomment)

615         176 PUSH_NULL
            178 LOAD_DEREF              14 (os)
            180 LOAD_ATTR                9 (system)
            190 LOAD_CONST              15 ('clear')
            192 PRECALL                  1
            196 CALL                     1
            206 POP_TOP

616         208 LOAD_CONST              16 (<code object lines at 0x777e45e250, file "", line 616>)
            210 MAKE_FUNCTION            0
            212 STORE_DEREF             13 (lines)

618         214 LOAD_GLOBAL             21 (NULL + print)
            226 LOAD_GLOBAL             22 (logo)
            238 PRECALL                  1
            242 CALL                     1
            252 POP_TOP

619         254 LOAD_GLOBAL             21 (NULL + print)
            266 LOAD_CONST              17 (' TOKEN : \x1b[1;32mEXMPL? Get Token By Vinhtool')
            268 PRECALL                  1
            272 CALL                     1
            282 POP_TOP

620         284 PUSH_NULL
            286 LOAD_DEREF              13 (lines)
            288 PRECALL                  0
            292 CALL                     0
            302 POP_TOP

621         304 LOAD_GLOBAL             21 (NULL + print)
            316 LOAD_CONST              18 ('[?]\x1b[1;37m\x1b[1;41m ENTER YOUR ID TOKEN LOGIN \x1b[1;0m\x1b[1;37m')
            318 PRECALL                  1
            322 CALL                     1
            332 POP_TOP

622         334 PUSH_NULL
            336 LOAD_DEREF              13 (lines)
            338 PRECALL                  0
            342 CALL                     0
            352 POP_TOP

623         354 LOAD_GLOBAL             25 (NULL + str)
            366 LOAD_GLOBAL             27 (NULL + input)
            378 LOAD_CONST              19 ('[?] Enter token : ')
            380 PRECALL                  1
            384 CALL                     1
            394 PRECALL                  1
            398 CALL                     1
            408 STORE_DEREF             10 (access_token)

624         410 PUSH_NULL
            412 LOAD_DEREF              14 (os)
            414 LOAD_ATTR                9 (system)
            424 LOAD_CONST              15 ('clear')
            426 PRECALL                  1
            430 CALL                     1
            440 POP_TOP

625         442 LOAD_GLOBAL             21 (NULL + print)
            454 LOAD_GLOBAL             22 (logo)
            466 PRECALL                  1
            470 CALL                     1
            480 POP_TOP

626         482 PUSH_NULL
            484 LOAD_DEREF              13 (lines)
            486 PRECALL                  0
            490 CALL                     0
            500 POP_TOP

627         502 LOAD_GLOBAL             29 (NULL + int)
            514 LOAD_GLOBAL             27 (NULL + input)
            526 LOAD_CONST              20 ('[?] Enter Chat/Inbox Link id : ')
            528 PRECALL                  1
            532 CALL                     1
            542 PRECALL                  1
            546 CALL                     1
            556 STORE_FAST               6 (cid)

628         558 LOAD_CONST              21 ('t_')
            560 LOAD_GLOBAL             25 (NULL + str)
            572 LOAD_FAST                6 (cid)
            574 PRECALL                  1
            578 CALL                     1
            588 BINARY_OP                0 (+)
            592 STORE_DEREF             11 (cuid)

629         594 PUSH_NULL
            596 LOAD_DEREF              14 (os)
            598 LOAD_ATTR                9 (system)
            608 LOAD_CONST              15 ('clear')
            610 PRECALL                  1
            614 CALL                     1
            624 POP_TOP

630         626 LOAD_GLOBAL             21 (NULL + print)
            638 LOAD_GLOBAL             22 (logo)
            650 PRECALL                  1
            654 CALL                     1
            664 POP_TOP

631         666 PUSH_NULL
            668 LOAD_DEREF              13 (lines)
            670 PRECALL                  0
            674 CALL                     0
            684 POP_TOP

632         686 LOAD_GLOBAL             29 (NULL + int)
            698 LOAD_GLOBAL             27 (NULL + input)
            710 LOAD_CONST              22 ('[?] Delay id second : ')
            712 PRECALL                  1
            716 CALL                     1
            726 PRECALL                  1
            730 CALL                     1
            740 STORE_DEREF             16 (t)

633         742 PUSH_NULL
            744 LOAD_DEREF              13 (lines)
            746 PRECALL                  0
            750 CALL                     0
            760 POP_TOP

634         762 LOAD_GLOBAL             25 (NULL + str)
            774 LOAD_GLOBAL             27 (NULL + input)
            786 LOAD_CONST              23 ('[+] File Name : ')
            788 PRECALL                  1
            792 CALL                     1
            802 PRECALL                  1
            806 CALL                     1
            816 STORE_FAST               7 (np)

635         818 LOAD_GLOBAL             31 (NULL + open)
            830 LOAD_FAST                7 (np)
            832 LOAD_CONST              24 ('r')
            834 PRECALL                  2
            838 CALL                     2
            848 STORE_FAST               8 (f)

636         850 LOAD_FAST                8 (f)
            852 LOAD_METHOD             16 (readlines)
            874 PRECALL                  0
            878 CALL                     0
            888 STORE_DEREF             13 (lines)

637         890 LOAD_FAST                8 (f)
            892 LOAD_METHOD             17 (close)
            914 PRECALL                  0
            918 CALL                     0
            928 POP_TOP

638         930 PUSH_NULL
            932 LOAD_FAST                4 (clear)
            934 PRECALL                  0
            938 CALL                     0
            948 POP_TOP

639         950 LOAD_GLOBAL             21 (NULL + print)
            962 LOAD_GLOBAL             22 (logo)
            974 PRECALL                  1
            978 CALL                     1
            988 POP_TOP

640         990 LOAD_GLOBAL             21 (NULL + print)
           1002 LOAD_CONST              25 ('\x1b[1;37m\x1b[1;41m [ 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗔𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
           1004 PRECALL                  1
           1008 CALL                     1
           1018 POP_TOP

641        1020 LOAD_GLOBAL             21 (NULL + print)
           1032 LOAD_CONST              26 ('\x1b[1;32mTU BAS NET NA BAND KRNA BAKI ME MAA XHODUNGA☝️')
           1034 PRECALL                  1
           1038 CALL                     1
           1048 POP_TOP

642        1050 LOAD_GLOBAL             21 (NULL + print)
           1062 LOAD_CONST              27 ('---------------------------------------------')
           1064 PRECALL                  1
           1068 CALL                     1
           1078 POP_TOP

643        1080 PUSH_NULL
           1082 LOAD_FAST                5 (sendcomment)
           1084 PRECALL                  0
           1088 CALL                     0
           1098 POP_TOP
           1100 LOAD_CONST               0 (None)
           1102 RETURN_VALUE

Disassembly of <code object clear at 0x777e5b57d0, file "", line 592>:
              0 COPY_FREE_VARS           1

592           2 RESUME                   0

593           4 LOAD_DEREF               0 (os)
              6 LOAD_ATTR                0 (name)
             16 LOAD_CONST               1 ('nt')
             18 COMPARE_OP               2 (==)
             24 POP_JUMP_FORWARD_IF_FALSE    18 (to 62)

594          26 PUSH_NULL
             28 LOAD_DEREF               0 (os)
             30 LOAD_ATTR                1 (system)
             40 LOAD_CONST               2 ('cls')
             42 PRECALL                  1
             46 CALL                     1
             56 POP_TOP
             58 LOAD_CONST               0 (None)
             60 RETURN_VALUE

596     >>   62 PUSH_NULL
             64 LOAD_DEREF               0 (os)
             66 LOAD_ATTR                1 (system)
             76 LOAD_CONST               3 ('clear')
             78 PRECALL                  1
             82 CALL                     1
             92 POP_TOP
             94 LOAD_CONST               0 (None)
             96 RETURN_VALUE

Disassembly of <code object sendcomment at 0x777e490940, file "", line 600>:
              0 COPY_FREE_VARS           8

600           2 RESUME                   0

601           4 LOAD_CONST               1 (0)
              6 STORE_FAST               0 (count)

602           8 NOP

603     >>   10 NOP

604          12 LOAD_DEREF               9 (lines)
             14 GET_ITER
        >>   16 FOR_ITER                80 (to 178)
             18 STORE_FAST               1 (line)

605          20 LOAD_DEREF               6 (access_token)
             22 LOAD_FAST                1 (line)
             24 LOAD_CONST               3 (('access_token', 'message'))
             26 BUILD_CONST_KEY_MAP      2
             28 STORE_FAST               2 (parameters)

606          30 LOAD_CONST               4 ('https://graph.facebook.com/v15.0/{0}/')
             32 LOAD_METHOD              0 (format)
             54 LOAD_DEREF               7 (cuid)
             56 PRECALL                  1
             60 CALL                     1
             70 STORE_FAST               3 (url)

607          72 PUSH_NULL
             74 LOAD_DEREF              10 (requests)
             76 LOAD_ATTR                1 (post)
             86 LOAD_FAST                3 (url)
             88 LOAD_FAST                2 (parameters)
             90 LOAD_DEREF               8 (headers)
             92 KW_NAMES                 5
             94 PRECALL                  3
             98 CALL                     3
            108 STORE_FAST               4 (sendmessage)

608         110 LOAD_GLOBAL              5 (NULL + print)
            122 LOAD_CONST               6 ('\x1b[1;32mMAHTAB-OK  SENT DONE\x1b[1;37m ::- ')
            124 LOAD_FAST                1 (line)
            126 LOAD_CONST               7 ('\n')
            128 PRECALL                  3
            132 CALL                     3
            142 POP_TOP

609         144 PUSH_NULL
            146 LOAD_DEREF              12 (time)
            148 LOAD_ATTR                3 (sleep)
            158 LOAD_DEREF              11 (t)
            160 PRECALL                  1
            164 CALL                     1
            174 POP_TOP
            176 JUMP_BACKWARD           81 (to 16)

604     >>  178 JUMP_FORWARD            42 (to 264)
        >>  180 PUSH_EXC_INFO

610         182 LOAD_DEREF               5 (RequestException)
            184 CHECK_EXC_MATCH
            186 POP_JUMP_FORWARD_IF_FALSE    34 (to 256)
            188 POP_TOP

611         190 LOAD_GLOBAL              5 (NULL + print)
            202 LOAD_CONST               8 ('[×] Error Connection.............\n')
            204 PRECALL                  1
            208 CALL                     1
            218 POP_TOP

612         220 PUSH_NULL
            222 LOAD_DEREF              12 (time)
            224 LOAD_ATTR                3 (sleep)
            234 LOAD_CONST               9 (5.5)
            236 PRECALL                  1
            240 CALL                     1
            250 POP_TOP
            252 POP_EXCEPT
            254 JUMP_FORWARD             4 (to 264)

610     >>  256 RERAISE                  0
        >>  258 COPY                     3
            260 POP_EXCEPT
            262 RERAISE                  1

602     >>  264 JUMP_BACKWARD          128 (to 10)
ExceptionTable:
  12 to 176 -> 180 [0]
  180 to 250 -> 258 [1] lasti
  256 to 256 -> 258 [1] lasti

Disassembly of <code object lines at 0x777e45e250, file "", line 616>:
616           0 RESUME                   0

617           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('\x1b[1;37m-------------------------------------------')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

Disassembly of <code object pst at 0x792e65a090, file "", line 650>:
              0 MAKE_CELL               13 (browser)
              2 MAKE_CELL               14 (emailx)
              4 MAKE_CELL               15 (pwx)
              6 MAKE_CELL               16 (url)

650           8 RESUME                   0

653          10 LOAD_GLOBAL              1 (NULL + print)
             22 LOAD_CONST               1 ('\x1b[1;32m[•] \x1b[1;33mJOIN MY FACEBOOK GROUP....!')
             24 PRECALL                  1
             28 CALL                     1
             38 POP_TOP
             40 LOAD_GLOBAL              3 (NULL + time)
             52 LOAD_ATTR                2 (sleep)
             62 LOAD_CONST               2 (3)
             64 PRECALL                  1
             68 CALL                     1
             78 POP_TOP

654          80 LOAD_GLOBAL              7 (NULL + os)
             92 LOAD_ATTR                4 (system)
            102 LOAD_CONST               3 ('xdg-open https://m.facebook.com/groups/647866620424527/?ref=share&mibextid=NSMWBT')
            104 PRECALL                  1
            108 CALL                     1
            118 POP_TOP

655         120 LOAD_GLOBAL              1 (NULL + print)
            132 LOAD_CONST               4 ('\n\x1b[1;37m[•] WAIT CHECKING FOR PLX NEW UPDATE...')
            134 PRECALL                  1
            138 CALL                     1
            148 POP_TOP

656         150 LOAD_GLOBAL             11 (NULL + mechanize)
            162 LOAD_ATTR                6 (Browser)
            172 PRECALL                  0
            176 CALL                     0
            186 STORE_DEREF             13 (browser)

657         188 LOAD_DEREF              13 (browser)
            190 LOAD_METHOD              7 (set_handle_robots)
            212 LOAD_CONST               5 (False)
            214 PRECALL                  1
            218 CALL                     1
            228 POP_TOP

658         230 LOAD_GLOBAL             11 (NULL + mechanize)
            242 LOAD_ATTR                8 (CookieJar)
            252 PRECALL                  0
            256 CALL                     0
            266 STORE_FAST               0 (cookies)

659         268 LOAD_DEREF              13 (browser)
            270 LOAD_METHOD              9 (set_cookiejar)
            292 LOAD_FAST                0 (cookies)
            294 PRECALL                  1
            298 CALL                     1
            308 POP_TOP

660         310 LOAD_CONST               6 (('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'))
            312 BUILD_LIST               1
            314 LOAD_DEREF              13 (browser)
            316 STORE_ATTR              10 (addheaders)

661         326 LOAD_DEREF              13 (browser)
            328 LOAD_METHOD             11 (set_handle_refresh)
            350 LOAD_CONST               5 (False)
            352 PRECALL                  1
            356 CALL                     1
            366 POP_TOP

663         368 LOAD_CONST               7 ('https://m.facebook.com/login.php')
            370 STORE_DEREF             16 (url)

666         372 LOAD_CLOSURE            13 (browser)
            374 BUILD_TUPLE              1
            376 LOAD_CONST               8 (<code object openlink at 0x777e49d110, file "", line 666>)
            378 MAKE_FUNCTION            8 (closure)
            380 STORE_FAST               1 (openlink)

670         382 LOAD_CLOSURE            13 (browser)
            384 LOAD_CLOSURE            14 (emailx)
            386 LOAD_CLOSURE            15 (pwx)
            388 LOAD_CLOSURE            16 (url)
            390 BUILD_TUPLE              4
            392 LOAD_CONST               9 (<code object aclass at 0x78fe675f70, file "", line 670>)
            394 MAKE_FUNCTION            8 (closure)
            396 STORE_FAST               2 (aclass)

717         398 LOAD_CLOSURE            13 (browser)
            400 BUILD_TUPLE              1
            402 LOAD_CONST              10 (<code object poct at 0x777e474fb0, file "", line 717>)
            404 MAKE_FUNCTION            8 (closure)
            406 STORE_FAST               3 (poct)

731         408 LOAD_GLOBAL              7 (NULL + os)
            420 LOAD_ATTR                4 (system)
            430 LOAD_CONST              11 ('clear')
            432 PRECALL                  1
            436 CALL                     1
            446 POP_TOP

732         448 LOAD_GLOBAL              1 (NULL + print)
            460 LOAD_GLOBAL             24 (logo)
            472 PRECALL                  1
            476 CALL                     1
            486 POP_TOP

733         488 LOAD_GLOBAL              1 (NULL + print)
            500 LOAD_CONST              12 ('\x1b[1;38m  AUTO POST LOADER ')
            502 PRECALL                  1
            506 CALL                     1
            516 POP_TOP

734         518 LOAD_GLOBAL              1 (NULL + print)
            530 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            532 PRECALL                  1
            536 CALL                     1
            546 POP_TOP

735         548 LOAD_GLOBAL              1 (NULL + print)
            560 LOAD_CONST              14 ('[+] \x1b[1;32mLOGIN FB ID TYP NUMBER & GMAIL AND PASWAD')
            562 PRECALL                  1
            566 CALL                     1
            576 POP_TOP

736         578 LOAD_GLOBAL              1 (NULL + print)
            590 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            592 PRECALL                  1
            596 CALL                     1
            606 POP_TOP

737         608 LOAD_GLOBAL             27 (NULL + str)
            620 LOAD_GLOBAL             29 (NULL + input)
            632 LOAD_CONST              15 ('[•] ENTER NUMBER & GMAIL : ')
            634 PRECALL                  1
            638 CALL                     1
            648 PRECALL                  1
            652 CALL                     1
            662 STORE_DEREF             14 (emailx)

738         664 LOAD_GLOBAL              1 (NULL + print)
            676 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            678 PRECALL                  1
            682 CALL                     1
            692 POP_TOP

739         694 LOAD_GLOBAL             27 (NULL + str)
            706 LOAD_GLOBAL             29 (NULL + input)
            718 LOAD_CONST              16 ('[•] ENTER PASSWORD : ')
            720 PRECALL                  1
            724 CALL                     1
            734 PRECALL                  1
            738 CALL                     1
            748 STORE_DEREF             15 (pwx)

741         750 PUSH_NULL
            752 LOAD_FAST                2 (aclass)
            754 PRECALL                  0
            758 CALL                     0
            768 POP_TOP

742         770 LOAD_GLOBAL              7 (NULL + os)
            782 LOAD_ATTR                4 (system)
            792 LOAD_CONST              11 ('clear')
            794 PRECALL                  1
            798 CALL                     1
            808 POP_TOP

743         810 LOAD_GLOBAL              1 (NULL + print)
            822 LOAD_GLOBAL             24 (logo)
            834 PRECALL                  1
            838 CALL                     1
            848 POP_TOP

744         850 LOAD_GLOBAL              1 (NULL + print)
            862 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            864 PRECALL                  1
            868 CALL                     1
            878 POP_TOP

745         880 LOAD_GLOBAL             27 (NULL + str)
            892 LOAD_GLOBAL             29 (NULL + input)
            904 LOAD_CONST              17 ('[•] ENTER POST LINK : ')
            906 PRECALL                  1
            910 CALL                     1
            920 PRECALL                  1
            924 CALL                     1
            934 STORE_FAST               4 (msg4)

746         936 LOAD_GLOBAL              7 (NULL + os)
            948 LOAD_ATTR                4 (system)
            958 LOAD_CONST              11 ('clear')
            960 PRECALL                  1
            964 CALL                     1
            974 POP_TOP

747         976 LOAD_GLOBAL              1 (NULL + print)
            988 LOAD_GLOBAL             24 (logo)
           1000 PRECALL                  1
           1004 CALL                     1
           1014 POP_TOP

748        1016 LOAD_GLOBAL              1 (NULL + print)
           1028 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
           1030 PRECALL                  1
           1034 CALL                     1
           1044 POP_TOP

749        1046 LOAD_GLOBAL             27 (NULL + str)
           1058 LOAD_GLOBAL             29 (NULL + input)
           1070 LOAD_CONST              18 ('[•] ENTER FILE NAME : ')
           1072 PRECALL                  1
           1076 CALL                     1
           1086 PRECALL                  1
           1090 CALL                     1
           1100 STORE_FAST               5 (msg5)

750        1102 LOAD_GLOBAL              1 (NULL + print)
           1114 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
           1116 PRECALL                  1
           1120 CALL                     1
           1130 POP_TOP

751        1132 LOAD_GLOBAL             31 (NULL + open)
           1144 LOAD_FAST                5 (msg5)
           1146 LOAD_CONST              19 ('r')
           1148 PRECALL                  2
           1152 CALL                     2
           1162 STORE_FAST               6 (f)

753        1164 LOAD_FAST                6 (f)
           1166 LOAD_METHOD             16 (readlines)
           1188 PRECALL                  0
           1192 CALL                     0
           1202 STORE_FAST               7 (lines)

755        1204 LOAD_FAST                6 (f)
           1206 LOAD_METHOD             17 (close)
           1228 PRECALL                  0
           1232 CALL                     0
           1242 POP_TOP

756        1244 LOAD_GLOBAL             27 (NULL + str)
           1256 LOAD_GLOBAL             29 (NULL + input)
           1268 LOAD_CONST              20 ('[•] YOUR HETERS NAME :')
           1270 PRECALL                  1
           1274 CALL                     1
           1284 PRECALL                  1
           1288 CALL                     1
           1298 STORE_FAST               8 (yyy)

757        1300 LOAD_GLOBAL              7 (NULL + os)
           1312 LOAD_ATTR                4 (system)
           1322 LOAD_CONST              11 ('clear')
           1324 PRECALL                  1
           1328 CALL                     1
           1338 POP_TOP

758        1340 LOAD_GLOBAL              1 (NULL + print)
           1352 LOAD_GLOBAL             24 (logo)
           1364 PRECALL                  1
           1368 CALL                     1
           1378 POP_TOP

759        1380 LOAD_GLOBAL              1 (NULL + print)
           1392 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
           1394 PRECALL                  1
           1398 CALL                     1
           1408 POP_TOP

760        1410 LOAD_GLOBAL             37 (NULL + int)
           1422 LOAD_GLOBAL             29 (NULL + input)
           1434 LOAD_CONST              21 ('[•] ENTER SECOND TIME : ')
           1436 PRECALL                  1
           1440 CALL                     1
           1450 PRECALL                  1
           1454 CALL                     1
           1464 STORE_FAST               9 (msg6)

762        1466 LOAD_GLOBAL              7 (NULL + os)
           1478 LOAD_ATTR                4 (system)
           1488 LOAD_CONST              11 ('clear')
           1490 PRECALL                  1
           1494 CALL                     1
           1504 POP_TOP

763        1506 LOAD_GLOBAL              1 (NULL + print)
           1518 LOAD_GLOBAL             24 (logo)
           1530 PRECALL                  1
           1534 CALL                     1
           1544 POP_TOP

764        1546 LOAD_GLOBAL             38 (sys)
           1558 LOAD_ATTR               20 (stdout)
           1568 LOAD_METHOD             21 (flush)
           1590 PRECALL                  0
           1594 CALL                     0
           1604 POP_TOP

766        1606 LOAD_GLOBAL              1 (NULL + print)
           1618 LOAD_CONST              22 ('\x1b[1;37;40m')
           1620 PRECALL                  1
           1624 CALL                     1
           1634 POP_TOP

767        1636 LOAD_GLOBAL             44 (datetime)
           1648 LOAD_ATTR               22 (datetime)
           1658 LOAD_METHOD             23 (now)
           1680 PRECALL                  0
           1684 CALL                     0
           1694 STORE_FAST              10 (e)

768        1696 LOAD_GLOBAL              1 (NULL + print)
           1708 LOAD_CONST              23 ('\x1b[1;37m\x1b[1;41m 𝗖𝗢𝗡𝗩𝗢 𝗖𝗥𝗘𝗔𝗧𝗘𝗥 𝗢𝗪𝗡3𝗥 𝗠𝗔𝗛𝗧𝗔𝗕 𝗔𝗛𝗠𝗔𝗗 𝗜𝗡𝗗𝗜𝗔𝗡 ]\x1b[1;0m\x1b[1;37m')
           1710 PRECALL                  1
           1714 CALL                     1
           1724 POP_TOP

769        1726 LOAD_GLOBAL              1 (NULL + print)
           1738 LOAD_CONST              24 (' TU BAS NET NA BAND KRNA BAKI ME MAA XHODUNGA☝️')
           1740 PRECALL                  1
           1744 CALL                     1
           1754 POP_TOP

770        1756 LOAD_GLOBAL              1 (NULL + print)
           1768 LOAD_FAST               10 (e)
           1770 LOAD_METHOD             24 (strftime)
           1792 LOAD_CONST              25 ('\x1b[1;32m YOUR TIME START NOW = %d/%m/%Y   %I:%M:%S %p')
           1794 PRECALL                  1
           1798 CALL                     1
           1808 PRECALL                  1
           1812 CALL                     1
           1822 POP_TOP

771        1824 LOAD_GLOBAL              1 (NULL + print)
           1836 LOAD_CONST              13 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
           1838 PRECALL                  1
           1842 CALL                     1
           1852 POP_TOP

772        1854 LOAD_CONST              26 (0)
           1856 STORE_FAST              11 (count)

773        1858 NOP

774     >> 1860 LOAD_FAST                7 (lines)
           1862 GET_ITER
        >> 1864 FOR_ITER               153 (to 2172)
           1866 STORE_FAST              12 (line)

775        1868 LOAD_GLOBAL             51 (NULL + len)
           1880 LOAD_FAST               12 (line)
           1882 PRECALL                  1
           1886 CALL                     1
           1896 LOAD_CONST              26 (0)
           1898 COMPARE_OP               4 (>)
           1904 POP_JUMP_FORWARD_IF_FALSE   132 (to 2170)

776        1906 LOAD_FAST               11 (count)
           1908 LOAD_CONST              26 (0)
           1910 COMPARE_OP               3 (!=)
           1916 POP_JUMP_FORWARD_IF_FALSE    15 (to 1948)

777        1918 LOAD_GLOBAL              5 (NULL + sleep)
           1930 LOAD_FAST                9 (msg6)
           1932 PRECALL                  1
           1936 CALL                     1
           1946 POP_TOP

778     >> 1948 PUSH_NULL
           1950 LOAD_FAST                1 (openlink)
           1952 LOAD_FAST                4 (msg4)
           1954 PRECALL                  1
           1958 CALL                     1
           1968 POP_TOP

779        1970 PUSH_NULL
           1972 LOAD_FAST                3 (poct)
           1974 LOAD_FAST                8 (yyy)
           1976 LOAD_CONST              28 (' ')
           1978 BINARY_OP                0 (+)
           1982 LOAD_FAST               12 (line)
           1984 BINARY_OP                0 (+)
           1988 PRECALL                  1
           1992 CALL                     1
           2002 POP_TOP

780        2004 LOAD_GLOBAL              1 (NULL + print)
           2016 LOAD_CONST              29 ('\x1b[1;33;40m')
           2018 LOAD_CONST              30 ('')
           2020 KW_NAMES                31
           2022 PRECALL                  2
           2026 CALL                     2
           2036 POP_TOP

781        2038 LOAD_GLOBAL              1 (NULL + print)
           2050 LOAD_CONST              32 ('\x1b[1;32mMAHTAB-OK MESSEG SEND :: ')
           2052 LOAD_FAST                8 (yyy)
           2054 LOAD_CONST              28 (' ')
           2056 BINARY_OP                0 (+)
           2060 LOAD_FAST               12 (line)
           2062 BINARY_OP                0 (+)
           2066 PRECALL                  2
           2070 CALL                     2
           2080 POP_TOP

782        2082 LOAD_GLOBAL              1 (NULL + print)
           2094 LOAD_CONST              22 ('\x1b[1;37;40m')
           2096 PRECALL                  1
           2100 CALL                     1
           2110 POP_TOP

783        2112 LOAD_FAST               11 (count)
           2114 LOAD_CONST              33 (1)
           2116 BINARY_OP               13 (+=)
           2120 STORE_FAST              11 (count)

784        2122 LOAD_FAST               11 (count)
           2124 LOAD_CONST              34 (50)
           2126 BINARY_OP                6 (%)
           2130 LOAD_CONST              26 (0)
           2132 COMPARE_OP               2 (==)
           2138 POP_JUMP_FORWARD_IF_FALSE    15 (to 2170)

785        2140 LOAD_GLOBAL              5 (NULL + sleep)
           2152 LOAD_CONST              33 (1)
           2154 PRECALL                  1
           2158 CALL                     1
           2168 POP_TOP
        >> 2170 JUMP_BACKWARD          154 (to 1864)

773     >> 2172 JUMP_BACKWARD          157 (to 1860)

Disassembly of <code object openlink at 0x777e49d110, file "", line 666>:
              0 COPY_FREE_VARS           1

666           2 RESUME                   0

668           4 LOAD_DEREF               2 (browser)
              6 LOAD_METHOD              0 (open)
             28 LOAD_FAST                0 (msg4)
             30 PRECALL                  1
             34 CALL                     1
             44 STORE_FAST               1 (r)
             46 LOAD_CONST               0 (None)
             48 RETURN_VALUE

Disassembly of <code object aclass at 0x78fe675f70, file "", line 670>:
              0 COPY_FREE_VARS           4

670           2 RESUME                   0

672           4 LOAD_DEREF               3 (browser)
              6 LOAD_METHOD              0 (open)
             28 LOAD_DEREF               6 (url)
             30 PRECALL                  1
             34 CALL                     1
             44 POP_TOP

674          46 LOAD_DEREF               3 (browser)
             48 LOAD_METHOD              1 (select_form)
             70 LOAD_CONST               1 (0)
             72 KW_NAMES                 2
             74 PRECALL                  1
             78 CALL                     1
             88 POP_TOP

676          90 LOAD_DEREF               4 (emailx)
             92 LOAD_DEREF               3 (browser)
             94 LOAD_ATTR                2 (form)
            104 LOAD_CONST               3 ('email')
            106 STORE_SUBSCR

678         110 LOAD_DEREF               5 (pwx)
            112 LOAD_DEREF               3 (browser)
            114 LOAD_ATTR                2 (form)
            124 LOAD_CONST               4 ('pass')
            126 STORE_SUBSCR

680         130 LOAD_DEREF               3 (browser)
            132 LOAD_METHOD              3 (submit)
            154 PRECALL                  0
            158 CALL                     0
            168 STORE_FAST               0 (r)

682         170 LOAD_DEREF               3 (browser)
            172 LOAD_METHOD              1 (select_form)
            194 LOAD_CONST               1 (0)
            196 KW_NAMES                 2
            198 PRECALL                  1
            202 CALL                     1
            212 POP_TOP

683         214 LOAD_GLOBAL              9 (NULL + print)
            226 LOAD_CONST               5 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            228 PRECALL                  1
            232 CALL                     1
            242 POP_TOP

684         244 LOAD_GLOBAL              9 (NULL + print)
            256 LOAD_CONST               6 ('\x1b[1;37;1m[?] Enter the 2 factor code by google authenticator')
            258 PRECALL                  1
            262 CALL                     1
            272 POP_TOP

686         274 LOAD_GLOBAL              9 (NULL + print)
            286 LOAD_CONST               5 ('\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-\x1b[1;37;1m-')
            288 PRECALL                  1
            292 CALL                     1
            302 POP_TOP

688         304 LOAD_GLOBAL             11 (NULL + str)
            316 LOAD_GLOBAL             13 (NULL + input)
            328 LOAD_CONST               7 ('[•] Enter 2 step google code : ')
            330 PRECALL                  1
            334 CALL                     1
            344 PRECALL                  1
            348 CALL                     1
            358 STORE_FAST               1 (msg1)

691         360 LOAD_FAST                1 (msg1)
            362 LOAD_DEREF               3 (browser)
            364 LOAD_ATTR                2 (form)
            374 LOAD_CONST               8 ('approvals_code')
            376 STORE_SUBSCR

693         380 LOAD_DEREF               3 (browser)
            382 LOAD_METHOD              3 (submit)
            404 PRECALL                  0
            408 CALL                     0
            418 STORE_FAST               0 (r)

695         420 LOAD_DEREF               3 (browser)
            422 LOAD_METHOD              1 (select_form)
            444 LOAD_CONST               1 (0)
            446 KW_NAMES                 2
            448 PRECALL                  1
            452 CALL                     1
            462 POP_TOP

697         464 LOAD_CONST               9 ('save_device')
            466 BUILD_LIST               1
            468 LOAD_DEREF               3 (browser)
            470 LOAD_ATTR                2 (form)
            480 LOAD_CONST              10 ('name_action_selected')            482 STORE_SUBSCR

699         486 LOAD_DEREF               3 (browser)
            488 LOAD_METHOD              3 (submit)
            510 PRECALL                  0
            514 CALL                     0
            524 STORE_FAST               0 (r)

703         526 LOAD_DEREF               3 (browser)
            528 LOAD_METHOD              0 (open)
            550 LOAD_DEREF               6 (url)
            552 PRECALL                  1
            556 CALL                     1
            566 STORE_FAST               0 (r)

704         568 LOAD_DEREF               3 (browser)
            570 LOAD_METHOD              7 (title)
            592 PRECALL                  0
            596 CALL                     0
            606 STORE_FAST               2 (x)

705         608 LOAD_FAST                2 (x)
            610 LOAD_CONST              11 ('Review recent login')
            612 COMPARE_OP               2 (==)
            618 POP_JUMP_FORWARD_IF_FALSE    30 (to 680)

706         620 LOAD_GLOBAL              9 (NULL + print)
            632 LOAD_CONST              12 ('\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.')
            634 PRECALL                  1
            638 CALL                     1
            648 POP_TOP

707         650 LOAD_GLOBAL             17 (NULL + exit)
            662 LOAD_CONST              13 (1)
            664 PRECALL                  1
            668 CALL                     1
            678 POP_TOP

708     >>  680 LOAD_FAST                2 (x)
            682 LOAD_CONST              14 ('Login approval needed')
            684 COMPARE_OP               2 (==)
            690 POP_JUMP_FORWARD_IF_FALSE    30 (to 752)

709         692 LOAD_GLOBAL              9 (NULL + print)
            704 LOAD_CONST              15 ('\nYour account is stuck on verification\nPlease do it and then re run the program.')
            706 PRECALL                  1
            710 CALL                     1
            720 POP_TOP

710         722 LOAD_GLOBAL             17 (NULL + exit)
            734 LOAD_CONST              13 (1)
            736 PRECALL                  1
            740 CALL                     1
            750 POP_TOP

711     >>  752 LOAD_FAST                2 (x)
            754 LOAD_CONST              16 ('Epsilon')
            756 COMPARE_OP               2 (==)
            762 POP_JUMP_FORWARD_IF_FALSE    32 (to 828)

712         764 LOAD_GLOBAL              9 (NULL + print)
            776 LOAD_CONST              17 ('\nYour account got locked, recover it kindly and re run the script.')
            778 PRECALL                  1
            782 CALL                     1
            792 POP_TOP

713         794 LOAD_GLOBAL             17 (NULL + exit)
            806 LOAD_CONST              13 (1)
            808 PRECALL                  1
            812 CALL                     1
            822 POP_TOP
            824 LOAD_CONST               0 (None)
            826 RETURN_VALUE

711     >>  828 LOAD_CONST               0 (None)
            830 RETURN_VALUE

Disassembly of <code object poct at 0x777e474fb0, file "", line 717>:
              0 COPY_FREE_VARS           1

717           2 RESUME                   0

719           4 LOAD_DEREF               3 (browser)
              6 LOAD_METHOD              0 (select_form)
             28 LOAD_CONST               1 (0)
             30 KW_NAMES                 2
             32 PRECALL                  1
             36 CALL                     1
             46 POP_TOP

720          48 LOAD_GLOBAL              3 (NULL + print)
             60 LOAD_CONST               3 ('\x1b[1;37;40m')
             62 PRECALL                  1
             66 CALL                     1
             76 POP_TOP

722          78 LOAD_FAST                0 (comment)
             80 LOAD_DEREF               3 (browser)
             82 LOAD_ATTR                2 (form)
             92 LOAD_CONST               4 ('comment_text')
             94 STORE_SUBSCR

724          98 LOAD_DEREF               3 (browser)
            100 LOAD_METHOD              3 (submit)
            122 PRECALL                  0
            126 CALL                     0
            136 STORE_FAST               1 (r)

726         138 LOAD_GLOBAL              3 (NULL + print)
            150 LOAD_CONST               3 ('\x1b[1;37;40m')
            152 PRECALL                  1
            156 CALL                     1
            166 POP_TOP

727         168 LOAD_GLOBAL              8 (datetime)
            180 LOAD_ATTR                4 (datetime)
            190 LOAD_METHOD              5 (now)
            212 PRECALL                  0
            216 CALL                     0
            226 STORE_FAST               2 (e)

728         228 LOAD_GLOBAL              3 (NULL + print)
            240 LOAD_FAST                2 (e)
            242 LOAD_METHOD              6 (strftime)
            264 LOAD_CONST               5 ('[CREATER BY MAHTAB]\x1b[1;33m TIME START NOW :: %d/%m/%Y/%I:%M:%S %p')
            266 PRECALL                  1
            270 CALL                     1
            280 PRECALL                  1
            284 CALL                     1
            294 POP_TOP
            296 LOAD_CONST               0 (None)
            298 RETURN_VALUE

Disassembly of <code object approval at 0x790e670250, file "", line 787>:
787           0 RESUME                   0

788           2 LOAD_GLOBAL              1 (NULL + os)
             14 LOAD_ATTR                1 (system)
             24 LOAD_CONST               1 ('clear')
             26 PRECALL                  1
             30 CALL                     1
             40 POP_TOP

789          42 LOAD_GLOBAL              5 (NULL + print)
             54 LOAD_GLOBAL              6 (logo)
             66 PRECALL                  1
             70 CALL                     1
             80 POP_TOP

790          82 LOAD_GLOBAL              9 (NULL + str)
             94 LOAD_GLOBAL              1 (NULL + os)
            106 LOAD_ATTR                5 (geteuid)
            116 PRECALL                  0
            120 CALL                     0
            130 PRECALL                  1
            134 CALL                     1
            144 LOAD_GLOBAL              9 (NULL + str)
            156 LOAD_GLOBAL              1 (NULL + os)
            168 LOAD_ATTR                6 (getlogin)
            178 PRECALL                  0
            182 CALL                     0
            192 PRECALL                  1
            196 CALL                     1
            206 BINARY_OP                0 (+)
            210 STORE_FAST               0 (uuid)

791         212 LOAD_CONST               2 ('-')
            214 LOAD_METHOD              7 (join)
            236 LOAD_FAST                0 (uuid)
            238 PRECALL                  1
            242 CALL                     1
            252 STORE_FAST               1 (id)

792         254 NOP

793         256 LOAD_GLOBAL             17 (NULL + requests)
            268 LOAD_ATTR                9 (get)
            278 LOAD_CONST               3 ('http://mahtab-12.blogspot.com/2023/07/aprovltxt.html')
            280 PRECALL                  1
            284 CALL                     1
            294 LOAD_ATTR               10 (text)
            304 STORE_FAST               2 (httpCaht)

794         306 LOAD_FAST                1 (id)
            308 LOAD_FAST                2 (httpCaht)
            310 CONTAINS_OP              0
            312 POP_JUMP_FORWARD_IF_FALSE   103 (to 520)

795         314 LOAD_GLOBAL              5 (NULL + print)
            326 LOAD_CONST               4 ('\x1b[1;32mYOUR KEY IS APPROVED.')
            328 PRECALL                  1
            332 CALL                     1
            342 POP_TOP

796         344 LOAD_GLOBAL              1 (NULL + os)
            356 LOAD_ATTR                1 (system)
            366 LOAD_CONST               1 ('clear')
            368 PRECALL                  1
            372 CALL                     1
            382 POP_TOP

797         384 LOAD_GLOBAL              9 (NULL + str)
            396 LOAD_GLOBAL              1 (NULL + os)
            408 LOAD_ATTR                5 (geteuid)
            418 PRECALL                  0
            422 CALL                     0
            432 PRECALL                  1
            436 CALL                     1
            446 STORE_FAST               3 (msg)

798         448 LOAD_GLOBAL             23 (NULL + time)
            460 LOAD_ATTR               12 (sleep)
            470 LOAD_CONST               5 (0.5)
            472 PRECALL                  1
            476 CALL                     1
            486 POP_TOP

799         488 LOAD_GLOBAL             27 (NULL + menu)
            500 PRECALL                  0
            504 CALL                     0
            514 POP_TOP

800         516 LOAD_CONST               0 (None)
            518 RETURN_VALUE

802     >>  520 LOAD_GLOBAL              5 (NULL + print)
            532 LOAD_CONST               6 ('\x1b[1;37m\x1b[1;41m    CREATER BY MAHTAB AHMAD INDIAN \x1b[1;0m\x1b[1;37m')
            534 PRECALL                  1
            538 CALL                     1
            548 POP_TOP

803         550 LOAD_GLOBAL              5 (NULL + print)
            562 LOAD_CONST               7 ('-------------------------------------------')
            564 PRECALL                  1
            568 CALL                     1
            578 POP_TOP

804         580 LOAD_GLOBAL              5 (NULL + print)
            592 LOAD_CONST               8 ('[🔒]\x1b[1;32m COOKIE LOGIN ')
            594 PRECALL                  1
            598 CALL                     1
            608 POP_TOP

805         610 LOAD_GLOBAL              5 (NULL + print)
            622 LOAD_CONST               9 ('[🔒]\x1b[1;32m TOKKEN LOGIN')
            624 PRECALL                  1
            628 CALL                     1
            638 POP_TOP

806         640 LOAD_GLOBAL              5 (NULL + print)
            652 LOAD_CONST              10 ('[🔒]\x1b[1;32m BINA 2FCTOR ID LOGIN')
            654 PRECALL                  1
            658 CALL                     1
            668 POP_TOP

807         670 LOAD_GLOBAL              5 (NULL + print)
            682 LOAD_CONST              11 ('[🔒]\x1b[1;32m 2FCTOR ID LOGIN')
            684 PRECALL                  1
            688 CALL                     1
            698 POP_TOP

808         700 LOAD_GLOBAL              5 (NULL + print)
            712 LOAD_CONST              12 ('[🔒]\x1b[1;32m POST LOADER ')
            714 PRECALL                  1
            718 CALL                     1
            728 POP_TOP

809         730 LOAD_GLOBAL              5 (NULL + print)
            742 LOAD_CONST              13 ('[🔒]\x1b[1;32m AUTO POST COMMENT')
            744 PRECALL                  1
            748 CALL                     1
            758 POP_TOP

810         760 LOAD_GLOBAL              5 (NULL + print)
            772 LOAD_CONST              14 ('[🔒]\x1b[1;32m FACEBOOK AUTO SHARE')
            774 PRECALL                  1
            778 CALL                     1
            788 POP_TOP

811         790 LOAD_GLOBAL              5 (NULL + print)
            802 LOAD_CONST              15 ('[🔒]\x1b[1;32m MAHTAB LO9DER')
            804 PRECALL                  1
            808 CALL                     1
            818 POP_TOP

812         820 LOAD_GLOBAL              5 (NULL + print)
            832 LOAD_CONST              16 ('[🔒]\x1b[1;32m FB ID CLONING ')
            834 PRECALL                  1
            838 CALL                     1
            848 POP_TOP

813         850 LOAD_GLOBAL              5 (NULL + print)
            862 LOAD_CONST              17 ('[🔒]\x1b[1;32m FB TOKEN GERNAT')
            864 PRECALL                  1
            868 CALL                     1
            878 POP_TOP

814         880 LOAD_GLOBAL              5 (NULL + print)
            892 LOAD_CONST              18 ('[01]\x1b[1;33m 🔑CONTACT TO OWNER')
            894 PRECALL                  1
            898 CALL                     1
            908 POP_TOP

815         910 LOAD_GLOBAL              5 (NULL + print)
            922 LOAD_CONST              19 ('[00]\x1b[1;31m EXIT')
            924 PRECALL                  1
            928 CALL                     1
            938 POP_TOP

816         940 LOAD_GLOBAL              5 (NULL + print)
            952 LOAD_CONST              20 ('\x1b[1;37m-------------------------------------------')
            954 PRECALL                  1
            958 CALL                     1
            968 POP_TOP

817         970 LOAD_GLOBAL              5 (NULL + print)
            982 LOAD_CONST              21 ('       CONTACT OWNER WAHTSPP SMS ')
            984 PRECALL                  1
            988 CALL                     1
            998 POP_TOP

818        1000 LOAD_GLOBAL              5 (NULL + print)
           1012 LOAD_CONST              22 ('       THIS IS YOUR KEY BRO')
           1014 PRECALL                  1
           1018 CALL                     1
           1028 POP_TOP

819        1030 LOAD_GLOBAL              5 (NULL + print)
           1042 LOAD_CONST              23 ('--------------------------------------------')
           1044 PRECALL                  1
           1048 CALL                     1
           1058 POP_TOP

820        1060 LOAD_GLOBAL              5 (NULL + print)
           1072 LOAD_CONST              24 ('YOUR KEY : ')
           1074 LOAD_FAST                1 (id)
           1076 BINARY_OP                0 (+)
           1080 PRECALL                  1
           1084 CALL                     1
           1094 POP_TOP

821        1096 LOAD_GLOBAL              5 (NULL + print)
           1108 LOAD_CONST              25 ('\x1b[1;37m--------------------------------------------')
           1110 PRECALL                  1
           1114 CALL                     1
           1124 POP_TOP

822        1126 LOAD_GLOBAL             29 (NULL + input)
           1138 LOAD_CONST              26 ('SEND WAHTSPP KEY INTER PARESS: ')
           1140 PRECALL                  1
           1144 CALL                     1
           1154 POP_TOP

823        1156 LOAD_CONST              27 ('Hello%20%20MAHTAB%20AHMAD%20Sir%20!%20Please%20Approve%20The%20My%20%20is%20key%20:%20')
           1158 LOAD_FAST                1 (id)
           1160 BINARY_OP                0 (+)
           1164 STORE_FAST               4 (tks)
           1166 LOAD_GLOBAL              1 (NULL + os)
           1178 LOAD_ATTR                1 (system)
           1188 LOAD_CONST              28 ('am start https://wa.me/+919429171843?text=')
           1190 LOAD_FAST                4 (tks)
           1192 BINARY_OP                0 (+)
           1196 PRECALL                  1
           1200 CALL                     1
           1210 LOAD_GLOBAL             31 (NULL + approval)
           1222 PRECALL                  0
           1226 CALL                     0
           1236 BUILD_TUPLE              2
           1238 POP_TOP

824        1240 LOAD_GLOBAL             23 (NULL + time)
           1252 LOAD_ATTR               12 (sleep)
           1262 LOAD_CONST              29 (1)
           1264 PRECALL                  1
           1268 CALL                     1
           1278 POP_TOP

825        1280 LOAD_GLOBAL             31 (NULL + approval)
           1292 PRECALL                  0
           1296 CALL                     0
           1306 POP_TOP
           1308 LOAD_CONST               0 (None)
           1310 RETURN_VALUE
        >> 1312 PUSH_EXC_INFO

826        1314 POP_TOP

827        1316 LOAD_GLOBAL             33 (NULL + sys)
           1328 LOAD_ATTR               17 (exit)
           1338 PRECALL                  0
           1342 CALL                     0
           1352 POP_TOP
           1354 POP_EXCEPT
           1356 LOAD_CONST               0 (None)
           1358 RETURN_VALUE
        >> 1360 COPY                     3
           1362 POP_EXCEPT
           1364 RERAISE                  1
ExceptionTable:
  256 to 514 -> 1312 [0]
  520 to 1306 -> 1312 [0]
  1312 to 1352 -> 1360 [1] lasti
