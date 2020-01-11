from database import db
from app import create_app
app = create_app()
db.init_app(app)
app.app_context().push()
from models import Strain, Plasmid, Gene

db.drop_all(bind=None)
db.create_all()

# Test strains
strain1 = Strain("E. coli", "Andrew", "2019-10-24", "It's hungry", "yes")
strain2 = Strain("S. aureus", "Andrew", "2019-10-23", "It's cool", "yes")

# Test plasmids
plasmid1 = Plasmid("ACTG", "TCTA", "Andrew", "2019-10-24", "some notes", "file.txt", "1,2")
plasmid2 = Plasmid("TTCA", "GGTA", "Andrew", "2019-10-24", "some more notes", "file2.txt", "3,4")

# Test genes
gene1 = Gene("A happy gene", "CCCA", "Andrew", "2019-10-23", "notes here", "file3.txt")
gene2 = Gene("A sad gene", "GTCA", "Andrew", "2019-10-23", "even more notes here", "file4.txt")

db.session.add_all([strain1, strain2, plasmid1, plasmid2, gene1, gene2])
db.session.commit()