from random import choice
from colorama import Fore


R = Fore.RED
Y = Fore.YELLOW
B = Fore.BLUE
RT = Fore.RESET
G = Fore.GREEN
C = Fore.CYAN

b1=f"""

{R}8 888888888o.      8 888888888o.          ,o888888o.        d888888o.
{G}8 8888    `^888.   8 8888    `^888.    . 8888     `88.    .`8888:' `88.
{R}8 8888        `88. 8 8888        `88. ,8 8888       `8b   8.`8888.   Y8
{G}8 8888         `88 8 8888         `88 88 8888        `8b  `8.`8888.
{R}8 8888          88 8 8888          88 88 8888         88   `8.`8888.
{G}8 8888          88 8 8888          88 88 8888         88    `8.`8888.
{R}8 8888         ,88 8 8888         ,88 88 8888        ,8P     `8.`8888.
{G}8 8888        ,88' 8 8888        ,88' `8 8888       ,8P  8b   `8.`8888.
{R}8 8888    ,o88P'   8 8888    ,o88P'    ` 8888     ,88'   `8b.  ;8.`8888
{G}8 888888888P'      8 888888888P'          `8888888P'      `Y8888P ,88P{RT}'
"""
b2=f"""
{R}d8888b. {C}d8888b.  {C}.d88b.  {R}.d8888.
{R}88  `8D {C}88  `8D .{C}8P  Y8. {R}88'  YP
{R}88   88 {C}88   88 {C}88    88 {R}`8bo.
{R}88   88 {C}88   88 {C}88    88   {R}`Y8b.
{R}88  .8D {C}88  .8D `{C}8b  d8' {R}db   8D
{R}Y8888D' {C}Y8888D'  {C}`Y88P'{R}  `8888Y'
"""

b3=f"""
{R} .S_sSSs   {G}  .S_sSSs   {R}   sSSs_sSSs   {G}   sSSs
{G}.SS~YS%%b  {R}.SS~YS%%b   {G} d%%SP~YS%%b   {R} d%%SP
{R}S%S   `S%b {G} S%S   `S%b {R} d%S'     `S%b {G} d%S'
{G}S%S    S%S {R} S%S    S%S {G} S%S       S%S {R} S%|
{R}S%S    S&S {G} S%S    S&S {R} S&S       S&S {G} S&S
{G}S&S    S&S {R} S&S    S&S {G} S&S       S&S {R} Y&Ss
{R}S&S    S&S {G} S&S    S&S {R} S&S       S&S {G} `S&&S
{G}S&S    S&S {R} S&S    S&S {G} S&S       S&S {R}   `S*S
{R}S*S    d*S {G} S*S    d*S {R} S*b       d*S {G}    l*S
{G}S*S   .S*S {R} S*S   .S*S {G} S*S.     .S*S {R}   .S*P
{R}S*S_sdSSS  {G} S*S_sdSSS  {R}  SSSbs_sdSSS  {G} sSS*S
{G}SSS~YSSY   {R} SSS~YSSY   {G}   YSSP~YSSY   {R} YSS'

"""
b4=f"""


{R}DDDDDDDDDDDDD        {R}DDDDDDDDDDDDD             {R}OOOOOOOOO        {C}SSSSSSSSSSSSSSS
{R}D{C}::::::::::::{R}DDD     {R}D{C}::::::::::::{R}DDD        OO:::::::::OO    {C}SS:::::::::::::::S
{R}D{C}:::::::::::::::{R}DD   {R}D{C}:::::::::::::::{R}DD    OO:::::::::::::OO {C}S:::::SSSSSS::::::S
{R}DDD{C}:::::{R}DDDDD{C}:::::{R}D  {R}DDD{C}:::::{R}DDDDD{C}:::::{R}D  {R}O:::::::OOO:::::::O{C}S:::::S     SSSSSSS
  {R}D{C}:::::{R}D    D{C}:::::{R}D   D{C}:::::{R}D    {R}D{C}:::::{R}D O::::::O   {R}O::::::O{C}S:::::S
  {R}D{C}:::::{R}D     D{C}:::::{R}D  D{C}:::::{R}D     {R}D{C}:::::{R}DO:::::O     {R}O:::::O{C}S:::::S
  {R}D{C}:::::{R}D     D{C}:::::{R}D  D{C}:::::{R}D     {R}D{C}:::::{R}DO:::::O     {R}O:::::O {C}S::::SSSS
  {R}D{C}:::::{R}D     D{C}:::::{R}D  D{C}:::::{R}D     {R}D{C}:::::{R}DO:::::O     {R}O:::::O  {C}SS::::::SSSSS
  {R}D{C}:::::{R}D     D{C}:::::{R}D  D{C}:::::{R}D     {R}D{C}:::::{R}DO:::::O     {R}O:::::O    {C}SSS::::::::SS
  {R}D{C}:::::{R}D     D{C}:::::{R}D  D{C}:::::{R}D     {R}D{C}:::::{R}DO:::::O     {R}O:::::O       {C}SSSSSS::::S
  {R}D{C}:::::{R}D     D{C}:::::{R}D  D{C}:::::{R}D     {R}D{C}:::::{R}DO:::::O     {R}O:::::O            {C}S:::::S
  {R}D{C}:::::{R}D    D{C}:::::{R}D   D{C}:::::{R}D    {R}D{C}:::::{R}D O::::::O   {R}O::::::O            {C}S:::::S
{R}DDD{C}:::::{R}DDDDD:::::D  {R}DDD{C}:::::{R}DDDDD{C}:::::{R}D  {R}O:::::::OOO:::::::{C}OSSSSSSS     S:::::S
{R}D{C}:::::::::::::::{R}{R}DD   D{C}:::::::::::::::{R}DD    {R}OO:::::::::::::OO {C}S::::::SSSSSS:::::S
{R}D{C}::::::::::::{R}DDD     D{C}::::::::::::{R}DDD        {R}OO:::::::::OO   {C}S:::::::::::::::SS
{R}DDDDDDDDDDDDD        {R}DDDDDDDDDDDDD             {R}OOOOOOOOO      {C}SSSSSSSSSSSSSSS
"""
def show_banner():
    banner_list = [b1, b2, b3, b4]
    print(choice(banner_list))

