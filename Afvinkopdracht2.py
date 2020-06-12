from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.Data import CodonTable
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["get"])
def eiwit_maker():
    """Geeft de eiwitsequentie van de opgegeven sequentie

    return:
    De eiwitsequentie
    """
    seq = request.args.get("seq", "")
    try:
        bio_dna = Seq(seq, IUPAC.ambiguous_dna)
        standard_trans_table = CodonTable.unambiguous_dna_by_name["Standard"]
        translate = bio_dna.translate(table=standard_trans_table)
    except:
        translate = "Geen geldige DNA sequentie"
    return render_template("Afvinkopdracht2.html", seq=seq, translate=translate)

def main():
    app.run(debug=True)
main()