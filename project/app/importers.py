# Standard Libary
import csv

# First-Party
import reversion

# Local
from .forms import BrotherForm
from .models import User


def import_contacts(path='/Users/dbinetti/Desktop/tau.csv'):
    user = User.objects.get(username='admin')
    with open(path, 'r') as f:
        next(f)
        reader = csv.reader(f)
        rows = [row for row in reader]
        for row in rows:
            name = " ".join([
                row[1].strip(),
                row[2].strip(),
            ]).strip()
            email = row[3].lower().strip()
            phone = row[4].replace('\xa0', '').strip()
            data = {
                'name': name,
                'email': email,
                'phone': phone,
            }
            form = BrotherForm(
                data=data,
            )
            if form.is_valid():
                with reversion.create_revision():
                    form.save()
                    reversion.set_user(user)
                    reversion.set_comment('Initial import')
