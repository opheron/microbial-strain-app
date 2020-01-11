from app import db, Strain

# CREATE
strain4 = Strain("E. colus", "Andrew", "2019-10-25", "It's new", "yes")
db.session.add(strain4)

# READ
all_strains = Strains.query.all()
print(all_strains)

