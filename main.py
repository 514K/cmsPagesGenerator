import urllib.parse
from urllib.parse import quote

template = """'ENCOMMENT'=>[ //COMMENT
            'ucode'=>'URLDECODE',
            'session_start'=>'ENCOMMENT',
            'service_1'=>'RUTEXT',
            'service_7'=>'RUTEXT',
            'service_9'=>'RUTEXT',
            'service_10'=>'RUTEXT',
            'service_11'=>'от 900 р.',
            'service_12'=>'1500',
            'service_template'=>'/views/service_page/main_service.php',
            'price' => '6 000'

        ],"""

with open("scoreLinks", "r", encoding="utf8") as f:
    for line in f:
        ruenlst = line.split(";")
        text = template
        text = text.replace("ENCOMMENT", ruenlst[1].replace("\n", ""))
        text = text.replace("COMMENT", ruenlst[0])
        text = text.replace("RUTEXT", ruenlst[0].replace("-", " ").capitalize())
        print(quote(ruenlst[0]))
        print(text)