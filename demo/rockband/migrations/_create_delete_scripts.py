
def make_bands(apps, schema_editor):
    Band = apps.get_model("rockband", "Band")
    Member = apps.get_model("rockband", "Member")
    rock_sugar = Band.objects.create(name="Rock Sugar")
    p1 = Member.objects.create(name="Jess Harnell", band=rock_sugar, age=52)
    p2 = Member.objects.create(name="Chuck Duran", band=rock_sugar, age=49)
    quartet = Band.objects.create(name="Thistle Quartet", can_rock=False)
    p1 = Member.objects.create(name="Laurie Rominger", age=28, band=quartet)
    Band.objects.create(name='WeirdAl')

def delete_all(apps, schema_editor):
    Band = apps.get_model("rockband", "Band")
    Member = apps.get_model("rockband", "Band")
    for b in Band.objects.all():
        b.delete()
    for m in Member.objects.all():
        m.delete()