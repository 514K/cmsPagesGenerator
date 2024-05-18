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

scoreText = ""
with open("scoreLinks", "r", encoding="utf8") as f:
    for line in f:
        ruenlst = line.split(";")
        text = template
        text = text.replace("ENCOMMENT", ruenlst[1].replace("\n", ""))
        text = text.replace("COMMENT", ruenlst[0])
        text = text.replace("RUTEXT", ruenlst[0].replace("-", " ").capitalize())
        text = text.replace("URLDECODE", quote(ruenlst[0]))
        scoreText = scoreText + text + "\n"
    f.close()

with open("pages.txt", "w", encoding="utf8") as f:
    f.write(scoreText)
    f.close()