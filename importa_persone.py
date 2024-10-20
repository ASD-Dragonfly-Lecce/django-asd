import csv

filepath = '/home/vincent/Dropbox/ASD Dragonfly Lecce 93168100753/20241019_Elenco_Tesserati.csv'

outfilepath = '/home/vincent/Dropbox/ASD Dragonfly Lecce 93168100753/persone_persona.csv'

with open(filepath, 'r', encoding='utf-16') as f:
    reader = csv.DictReader(f, delimiter="\t")

    with open(outfilepath, 'w', encoding='utf-16') as out:
        outwriter = csv.writer(out, delimiter="\t")
        outwriter.writerow([
            'id', 'nome', 'cognome', 'sesso', 'datanascita', 
            'comunenascita', 'codicefiscale', 'entetessera',
            'codicetessera', 'datariltessera', 'indirizzo', 'comune',
            'tel', 'cell', 'email1', 'email2', 'creato_il', 'modificato_il', 'note',
            'creatore_id', 'stato', 'volontario', 'certmedico_scadenza', 'tutore1_id', 'tutore2_id', 'attivita'
        ])
        for idx, line in enumerate(reader, start=1):

            parts = (line['Nato il'].split('/'))
            parts.reverse()
            datanascita = "-".join(parts)

            parts = (line['Rilascio'].split('/'))
            parts.reverse()
            datariltessera = "-".join(parts)

            outwriter.writerow([
                idx,
                line['Nome'],
                line['Cognome'],
                line['Sesso'],
                datanascita,
                line['Nato a'],
                line['Codice fiscale'],
                'CSI Terra d\'Otranto',
                line['Tessera'],
                datariltessera,
                line['Indirizzo'],
                line['Comune'],
                line['Telefono'],
                line['Telefono'],
                line['email'],
                '',
                '2024-10-19',
                '2024-10-19',
                '',
                1,
                'attivo',
                0,
                None,
                None,
                None,
                line['Attività'],
            ])