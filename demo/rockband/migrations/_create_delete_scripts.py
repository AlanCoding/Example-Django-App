
def make_bands(apps, schema_editor):
    Band = apps.get_model("rockband", "Band")
    Member = apps.get_model("rockband", "Member")
    rock_sugar = Band.objects.create(name="Rock Sugar")
    p1 = Member.objects.create(name="Jess Harnell", band=rock_sugar)
    p2 = Member.objects.create(name="Chuck Duran", band=rock_sugar)

def delete_all(apps, schema_editor):
    Band = apps.get_model("rockband", "Band")
    Member = apps.get_model("rockband", "Band")
    for b in Band.objects.all():
        b.delete()
    for m in Member.objects.all():
        m.delete()