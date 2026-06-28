'''Generate all three zero-dollar business launch kits'''

from pathlib import Path
import csv, textwrap

base = Path('/root/ai-holding-company/businesses')
base.mkdir(parents=True, exist_ok=True)

# Shared artifacts
shared = base/'shared'
(shared/'templates').mkdir(parents=True, exist_ok=True)
(shared/'data').mkdir(parents=True, exist_ok=True)

# 1. Appointment Setting
appt = base/'appointment-setting'
for sub in ['data','templates','sop','agent_roster']:
    (appt/sub).mkdir(parents=True, exist_ok=True)

(appt/'README.md').write_text(textwrap.dedent('''\
# AI Appointment Setting Agency — $0 Launch Kit

## Business Model
You sell booked appointments for local/professional service businesses.
Charge $100-$300 per qualified appointment, then convert to monthly retainer.

## First Vertical Targets
- Roofing companies
- Plumbers
- HVAC
- Med spas
- Dentists

## Startup Cost
$0 using free email accounts, manual research, and guided outreach.
'''))

# Lead list template for appointment-setting clients
with (appt/'data/appointment_setting_lead_list_template.csv').open('w', newline='') as f:
    w=csv.DictWriter(f, ['business_name','owner_name','phone','email','website','niche','city','state','notes'])
    w.writeheader()
    w.writerow({'business_name':'','owner_name':'','phone':'','email':'','website':'','niche':'','city':'','state':'','notes':''})

# 2. Lead Gen Broker
leads = base/'lead-generation-broker'
for sub in ['data','templates','sop','agent_roster']:
    (leads/sub).mkdir(parents=True, exist_ok=True)

(leads/'README.md').write_text(textwrap.dedent('''\
# AI Lead Generation Broker — $0 Launch Kit

## Business Model
You find high-intent leads and sell them to businesses that need them.
Charge $20-$500 per lead depending on industry and value.

## First Lead Types
1. Homeowners needing roof replacement
2. Businesses needing new websites
3. Companies hiring dispatchers

## Startup Cost
$0 using public records, free directories, manual research, and email.
'''))

# 3. Recruiting
rec = base/'recruiting'
for sub in ['data','templates','sop','agent_roster']:
    (rec/sub).mkdir(parents=True, exist_ok=True)

(rec/'README.md').write_text(textwrap.dedent('''\
# AI Recruiter — $0 Launch Kit

## Business Model
You find candidates and help companies hire.
Charge flat fee, placement fee, or monthly recruiting support.

## First Placements
- Dispatchers
- Remote customer service
- Skilled trades
- Administrative roles

## Startup Cost
$0 using public job boards, free databases, LinkedIn (limited), and email.
'''))

# Shared compliance
(shared/'COMPLIANCE.md').write_text(textwrap.dedent('''\
# Compliance Rules For All Three Models

## Cold Email Rules (United States)
- Use your real name and company identity.
- Do not use deceptive subject lines or fake headers.
- Include a clear unsubscribe/opt-out method.
- Honor opt-outs immediately.
- Do not scrape or buy non-permissioned lists.
- Only send targeted, relevant outreach.

## Cold Calling Rules (United States)
- B2B manual cold calling is generally allowed.
- Place calls during legal hours only (8am-9pm local recipient time).
- Honor do-not-contact requests immediately.
- Do not use prerecorded or AI-generated voice for cold outbound.
- Do not spoof caller ID or use number rotation.

## Data Rules
- Use public, free, or permission-granted data only.
- Do not scrape sites that prohibit it.
- Do not use data for unauthorized marketing.

## Identity
We operate as Revenue Rescue Desk.
All outreach must be truthful, professional, and value-focused.
'''))

# Sample outreach templates
(shared/'templates/initial_outreach_email.txt').write_text(textwrap.dedent('''\
Subject: Quick question about {business_type} at {company_name}

Hi {contact_name},

My name is Brian Hamilton, and I work with a small number of {business_type} companies to help with {value_statement}.

I noticed {company_name} is active in {city}, and I thought there might be a fit. I am not selling anything in this email — I am simply testing whether one specific issue is relevant to your team.

Do you currently have a short problem to solve around {specific_topic}?

If not, no need to reply at all. If yes, I can send a one-page note on how other {business_type}s are handling it now.

Either way, I appreciate your time.

Brian Hamilton
Client Response Coordinator
Revenue Rescue Desk
{email_signature}
'''))

(shared/'templates/follow_up_email.txt').write_text(textwrap.dedent('''\
Subject: Re: Quick question about {business_type} at {company_name}

Hi {contact_name},

I wanted to follow up briefly in case my last note got buried.

I only need two minutes of your time. I have one specific idea for {company_name} around {specific_topic}, and if it is not useful you will not hear from me again.

Would it be okay to send that short note?

Best,
Brian Hamilton
Client Response Coordinator
Revenue Rescue Desk
{email_signature}
'''))

print('Created all three business launch kits')
for p in sorted(base.glob('*')): print(p)
print(shared)
