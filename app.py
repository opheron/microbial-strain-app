import os
from flask import Flask, render_template, request, flash, redirect, url_for
from models import Strain, Plasmid, Gene
from werkzeug.utils import secure_filename
from database import db

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    # This should be set as an env variable in production
    app.secret_key = "super secret key"

    app.config['UPLOAD_FOLDER'] = os.path.join(basedir, "uploads")
    # Max size of file to be uploaded - currently set to 25 MB
    app.config['MAX_CONTENT_PATH'] = 25 * 1024 * 1024
    # Not sure of the exact file extension to be used so I included the different Snapgene formats I could find

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()
db.init_app(app)

ALLOWED_EXTENSIONS = {'txt', 'ab1', 'abi', 'fa', 'fasta'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/strains', methods=["POST", "GET"])
def strains():
    if request.method == "GET":
        strains = Strain.query.all()
        return render_template('display_strains.html', strains=strains)
    elif request.method == "POST":
        description = request.form.get("description")
        created_by = request.form.get("created_by")
        creation_date = request.form.get("creation_date")
        notes = request.form.get("notes")
        contains_plasmids = request.form.get("contains_plasmids")
        new_strain = Strain(description, created_by, creation_date, notes, contains_plasmids)
        db.session.add(new_strain)
        db.session.commit()
        flash("Success!")
        return redirect("/")

@app.route('/strains/create')
def create_strain():
    return render_template('create_strain.html')

@app.route('/plasmids', methods=["POST", "GET"])
def plasmids():
    if request.method == "GET":
        plasmids = Plasmid.query.all()
        return render_template('display_plasmids.html', plasmids=plasmids)
    elif request.method == "POST":
        insert = request.form.get("insert")
        promoter = request.form.get("promoter")
        created_by = request.form.get("created_by")
        creation_date = request.form.get("creation_date")
        notes = request.form.get("notes")
        files = request.files.getlist('files[]')
        snapgene_files = ""
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                snapgene_files += filename + ","
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], "plasmids", filename))
        contains_genes = request.form.get("contains_genes")
        new_plasmid = Plasmid(insert, promoter, created_by, creation_date, notes, snapgene_files, contains_genes)
        db.session.add(new_plasmid)
        db.session.commit()
        flash("Success!")
        return redirect("/")

@app.route('/plasmids/create')
def create_plasmid():
    return render_template('create_plasmid.html')

@app.route('/genes', methods=["POST", "GET"])
def genes():
    if request.method == "GET":
        genes = Gene.query.all()
        return render_template('display_genes.html', genes=genes)
    elif request.method == "POST":
        description = request.form.get("description")
        dna_sequence = request.form.get("dna_sequence")
        created_by = request.form.get("created_by")
        creation_date = request.form.get("creation_date")
        notes = request.form.get("notes")
        files = request.files.getlist('files[]')
        snapgene_files = ""
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                snapgene_files += filename + ","
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], "plasmids", filename))
        contains_genes = request.form.get("contains_genes")
        new_gene = Gene(description, dna_sequence, created_by, creation_date, notes, snapgene_files)
        db.session.add(new_gene)
        db.session.commit()
        flash("Success!")
        return redirect("/")

@app.route('/genes/create')
def create_gene():
    return render_template('create_gene.html')

if __name__ == '__main__':
    app.run(debug = True)