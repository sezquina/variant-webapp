# app.py

from flask import Flask
from flask import request, render_template, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig

import string, re

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ensembl/')
@app.route('/ensembl/<string:gene>', methods=['GET'])
def ensembl(gene):
    results = variants.query.filter(variants.Gene_ensGene == gene).all()
    return render_template('ensembl.html', results=results)

@app.route('/variant/<string:variant>', methods=['GET'])
def variant(variant):
    results = variants.query.filter(variants.avsnp144 == variant).all()    
    return render_template('variant.html', variant=variant)

@app.route('/grange/')
@app.route('/grange/<string:chromosome>/<int:start>/<int:end>', methods=['GET'])
def grange(chromosome, start, end):
    results = variants.query.filter(variants.Chr == chromosome).filter(variants.Start > start).filter(variants.End < end).all()
    return render_template('grange.html', results=results)

def get_chr_coordinates_from_string(s):
    '''
    Returns chromosome coordinates from a given string.
    Coordinates have to be in "chr0:0000-0000" style!
    '''
    regex_for_chr       = re.compile('chr[0-9a-zA-Z_]*:')
    regex_for_start_end = re.compile('chr[0-9a-zA-Z_]*:[0-9]+-[0-9]+')
    chr     = re.search(regex_for_chr, s).group().replace(':', '')
    start, end = re.search(regex_for_start_end, s).group().split(':')[1].split('-')
    return(chr, start, end)

@app.route('/query', methods=['POST'])
def search():
    # strip leading/trailing whitespace and lowercase for processing
    query = str(request.form['query']).strip().lower()

    # if ENSEMBL gene
    x = re.findall("(^ensg\d+)", query)
    if len(x):
        results = variants.query.filter(variants.Gene_ensGene == x[0].upper()).all()
        return render_template('query.html', query=x[0].upper(), results=results)
    
    # if variant
    x = re.findall("(^rs\d+)", query)
    if len(x):
        results = variants.query.filter(variants.avsnp144 == x[0]).all()
        return render_template('query.html', query=x, results=results)
    
    # if genomic range
    x = re.findall("(^chr\w*)", query)
    if len(x):
        try:
            x = get_chr_coordinates_from_string(query)
            results = variants.query.filter(variants.Chr == re.sub("chr", "", x[0])).filter(variants.Start > x[1]).filter(variants.End < x[2]).all()
            return render_template('query.html', query=x, results=results)            
            #return redirect(url_for('grange', chromosome=re.sub("chr", "", x[0]), start=x[1], end=x[2]))
        except:
            x=0
    else:
        try:
            x = get_chr_coordinates_from_string("chr"+query)
            results = variants.query.filter(variants.Chr == re.sub("chr", "", x[0])).filter(variants.Start > x[1]).filter(variants.End < x[2]).all()
            return render_template('query.html', query=x, results=results)
            #return redirect(url_for('grange', chromosome=re.sub("chr", "", x[0]), start=x[1], end=x[2]))
        except:
            x=0
    
    # no other matches means probably a refseq gene
    results = variants.query.filter(variants.Gene_refGene == query.upper()).all()
    return render_template('query.html', query=query.upper(), results=results)
    #results = variants.query.filter(variants.Chr == '1').filter(variants.Start > 17000).filter(variants.End < 17300).all()
    #return render_template('query.html', query=query, results=results)
    return None

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    #app.run()
    app.run(host="0.0.0.0", port=8000, debug=True)
