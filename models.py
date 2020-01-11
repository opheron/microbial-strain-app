from database import db

class Strain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_by = db.Column(db.String)
    creation_date = db.Column(db.String)
    notes = db.Column(db.String)
    contains_plasmids = db.Column(db.String)

    def __init__(self, description, created_by, creation_date, notes, contains_plasmids):
        self.description = description
        self.created_by = created_by
        self.creation_date = creation_date
        self.notes = notes
        self.contains_plasmids = contains_plasmids

    def __repr__self():
        return "Strain " + self.id

class Plasmid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    insert = db.Column(db.String)
    promoter = db.Column(db.String)
    created_by = db.Column(db.String)
    creation_date = db.Column(db.String)
    notes = db.Column(db.String)
    snapgene_files = db.Column(db.String)
    contains_genes = db.Column(db.String)

    def __init__(self, insert, promoter, created_by, creation_date, notes, snapgene_files, contains_genes):
        self.insert = insert
        self.promoter = promoter
        self.created_by = created_by
        self.creation_date = creation_date
        self.notes = notes
        self.snapgene_files = snapgene_files
        self.contains_genes = contains_genes

class Gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    dna_sequence = db.Column(db.String)
    created_by = db.Column(db.String)
    creation_date = db.Column(db.String)
    notes = db.Column(db.String)
    snapgene_files = db.Column(db.String)

    def __init__(self, description, dna_sequence, created_by, creation_date, notes, snapgene_files):
        self.description = description
        self.dna_sequence = dna_sequence
        self.created_by = created_by
        self.creation_date = creation_date
        self.notes = notes
        self.snapgene_files = snapgene_files