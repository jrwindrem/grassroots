import requests
import csv
from legislators.models import Legislator
from bills.models import Bill

SUNLIGHT_API_KEY='6b879d65c49742058a88a0b955b3f172'
BASE_API_STR = 'http://congress.api.sunlightfoundation.com/'

def query_api(query, page):
    return requests.get('{}{}?apikey={}&per_page=50&page={}'.format(BASE_API_STR, query, SUNLIGHT_API_KEY, page))

def create_leg_object(obj):
    Legislator.objects.create(
        bioguide_id=obj['bioguide_id'],
        birthday=obj['birthday'],
        chamber=obj['chamber'],
        contact_form=obj['contact_form'],
        crp_id=obj['crp_id'],
        fax=obj['fax'],
        first_name=obj['first_name'],
        gender=obj['gender'],
        govtrack_id=obj['govtrack_id'],
        in_office=obj['in_office'],
        last_name=obj['last_name'],
        leadership_role=obj['leadership_role'],
        middle_name=obj['middle_name'],
        name_suffix=obj['name_suffix'],
        nickname=obj['nickname'],
        oc_email=obj['oc_email'],
        ocd_id=obj['ocd_id'],
        office=obj['office'],
        party=obj['party'],
        phone=obj['phone'],
        state=obj['state'],
        state_name=obj['state_name'],
        term_end=obj['term_end'],
        term_start=obj['term_start'],
        thomas_id=obj['thomas_id'],
        title=obj['title']
    )

def read_from_csv():
    with open('legislators.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row[0] == 'Rep':
                chamber = 'H'
            elif row[0] == 'Sen':
                chamber = 'S'
            else:
                chamber = 'O'

            _, created = Legislator.objects.get_or_create(
                chamber=chamber,
                title=row[0],
                first_name=row[1],
                middle_name=row[2],
                last_name=row[3],
                name_suffix=row[4],
                nickname=row[5],
                party=row[6],
                state=row[7],
                district=row[8],
                in_office=bool(int(row[9])),
                gender=row[10],
                phone=row[11],
                fax=row[12],
                website=row[13],
                contact_form=row[14],
                office=row[15],
                bioguide_id=row[16],
                govtrack_id=row[19],
                crp_id=row[20],
                twitter_id=row[21],
                facebook_id=row[24],
                birthday=row[27],
                oc_email=row[28]
            )

def create_bills(page):
    r = query_api('bills', page).json()['results']
    for bill in r:
        Bill.objects.get_or_create(
                bill_id = bill['bill_id'],
                defaults = {
                        'bill_type': bill['bill_type'],
                        'chamber': bill['chamber'],
                        'congress': bill['congress'],
                        'cosponsors_count': bill['cosponsors_count'],
                        'enacted_as': bill['enacted_as'],
                        'introduced_on': bill['introduced_on'][0:10],
                        'last_action_at': bill['last_action_at'][0:10],
                        'last_version_on': bill['last_version_on'][0:10],
                        'last_vote_at': bill['last_vote_at'][0:10] if bill['last_vote_at'] else None,
                        'number': bill['number'],
                        'official_title': bill['official_title'],
                        'popular_title': bill['popular_title'],
                        'short_title': bill['short_title'],
                        'sponsor': Legislator.objects.get(bioguide_id=bill['sponsor_id']),
                    }
                )
