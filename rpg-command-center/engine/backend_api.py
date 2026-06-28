#!/usr/bin/env python3
"""
RPG Command Center Backend API
Serves game state, executes real business ops, syncs backend to frontend.
"""

from pathlib import Path
import json, csv, subprocess, tomllib
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

ROOT = Path('/root/ai-holding-company')
GAME_STATE = ROOT / 'rpg-command-center/engine/public/game_state.json'
EVENT_LOG = ROOT / 'rpg-command-center/engine/logs/agent_dialogue.jsonl'
AGENCY_AGENT_DIR = Path('/root/agency-agents/integrations/codex/agents')

BUSINESS_AGENT_SLUGS = {
    'chief-of-staff': 'Coordinating the AI holding-company operating cadence and routing decisions.',
    'sales-outreach': 'Preparing compliant appointment-setting outreach assets; no emails/calls are sent from the game.',
    'operations-manager': 'Maintaining delivery SOPs, safe automation, and fulfillment handoffs.',
    'offer-lead-gen-strategist': 'Researching public lead criteria and pipeline quality for repeatable offers.',
    'finance-tracker': 'Watching gold, revenue targets, and model-cost discipline.',
    'support-responder': 'Protecting retention, client satisfaction, and support follow-up loops.',
    'pricing-analyst': 'Checking offer pricing, margins, and simple retainer economics.',
    'legal-compliance-checker': 'Guarding outreach rules: no unauthorized AI calls, no spoofing, no KYC/paywall bypass.',
    'recruitment-specialist': 'Designing recruiting-support offers and fulfillment checklists.',
    'reality-checker': 'Reality-checking launch claims before Brian sees them; defaulting to NEEDS WORK unless evidence is strong.',
    'evidence-collector': 'Collecting screenshots, endpoint outputs, and concrete proof for RPG/business changes.',
    'api-tester': 'Validating backend API health, action routes, asset MIME types, and failure handling.',
    'analytics-reporter': 'Turning revenue, lead, quest, and event data into concise operating reports.',
    'test-results-analyzer': 'Reading verification output and converting failures into clear next fixes.',
    'accessibility-auditor': 'Checking the RPG dashboard for keyboard access, readable labels, and WCAG-friendly UI cues.',
    'executive-summary-generator': 'Summarizing RPG/business progress into short Brian-ready operating reports.',
    'performance-benchmarker': 'Watching frontend/backend responsiveness and flagging slow or brittle loops.',
    'workflow-optimizer': 'Improving repeatable RPG build and business-operation workflows without adding paid tools.',
    'tool-evaluator': 'Evaluating zero-cost tools and asset pipelines before anything paid or KYC-heavy is used.',
    'growth-hacker': 'Designing safe demand-generation experiments and manual-review growth loops.',
    'content-creator': 'Preparing truthful website, offer, and sample-report copy for portfolio businesses.',
    'seo-specialist': 'Improving search-readiness and local/public content structure without citation guarantees.',
    'customer-success-manager': 'Designing onboarding, health-score, QBR, and retention workflows for future clients.',
    'business-strategist': 'Choosing the highest-probability recurring-revenue beachhead and keeping the portfolio focused on cash flow.',
    'outbound-strategist': 'Designing compliant outbound motions, segmentation, and approval queues without sending cold messages from the RPG.',
    'discovery-coach': 'Preparing beginner-proof discovery call scripts, qualifying questions, and objection drills for Brian.',
    'deal-strategist': 'Turning qualified conversations into simple pilot offers, proposal paths, and next-step commitments.',
    'pipeline-analyst': 'Maintaining funnel stages, lead quality signals, and next-action hygiene across prepared sales assets.',
    'proposal-strategist': 'Drafting truthful proposal outlines, scopes, exclusions, and decision-ready business cases.',
    'sales-engineer': 'Translating technical service delivery into buyer-friendly demos, evidence, and implementation notes.',
    'account-strategist': 'Planning expansion and retention plays once a client relationship exists.',
    'ai-citation-strategist': 'Auditing AI-search visibility snapshots and drafting citation-likelihood fixes without guaranteeing AI engine placement.',
    'agentic-search-optimizer': 'Auditing public website task flows for agent-readiness and WebMCP-style action clarity using safe manual review.',
    'aeo-foundations-architect': 'Preparing llms.txt, AI crawler, structured Markdown, and discovery-file readiness checklists for public websites.',
    'automation-governance-architect': 'Reviewing which acquisition and fulfillment automations should stay human-gated before any live execution.',
    'chief-financial-officer': 'Setting portfolio cash discipline, runway logic, margins, and revenue target governance.',
    'compliance-auditor': 'Auditing business processes for policy, privacy, and outreach-risk gaps before execution.',
    'data-privacy-officer': 'Protecting lead/client data handling, retention, consent, and privacy-safe operating defaults.',
    'document-generator': 'Generating clean client-facing templates, reports, checklists, and SOP documents from approved inputs.',
    'frontend-developer': 'Improving the playable canvas UI, keyboard/click interactions, dialogs, and frontend performance for Agent Farm.',
    'ux-researcher': 'Auditing Brian’s RPG dashboard flow for clarity, approachability, readability, and low-friction owner decisions.',
    'software-architect': 'Keeping the command-center architecture simple, maintainable, and tied to real backend business state.',
    'backend-architect': 'Hardening API contracts, state persistence, event logging, and safe action routes behind the RPG world.',
}

AGENT_POSITIONS = {
    'chief-of-staff': (25, 35),
    'sales-outreach': (70, 30),
    'operations-manager': (35, 70),
    'offer-lead-gen-strategist': (75, 65),
    'finance-tracker': (14, 25),
    'support-responder': (84, 76),
    'pricing-analyst': (21, 72),
    'legal-compliance-checker': (58, 76),
    'recruitment-specialist': (82, 48),
    'reality-checker': (47, 22),
    'evidence-collector': (44, 28),
    'api-tester': (51, 28),
    'analytics-reporter': (18, 64),
    'test-results-analyzer': (54, 28),
    'accessibility-auditor': (55, 22),
    'executive-summary-generator': (21, 59),
    'performance-benchmarker': (61, 28),
    'workflow-optimizer': (40, 78),
    'tool-evaluator': (66, 72),
    'growth-hacker': (73, 42),
    'content-creator': (78, 24),
    'seo-specialist': (86, 32),
    'customer-success-manager': (88, 68),
    'business-strategist': (29, 18),
    'outbound-strategist': (65, 18),
    'discovery-coach': (68, 38),
    'deal-strategist': (63, 48),
    'pipeline-analyst': (72, 54),
    'proposal-strategist': (58, 56),
    'sales-engineer': (78, 58),
    'account-strategist': (82, 62),
    'ai-citation-strategist': (89, 39),
    'agentic-search-optimizer': (91, 46),
    'aeo-foundations-architect': (87, 54),
    'automation-governance-architect': (60, 88),
    'chief-financial-officer': (16, 36),
    'compliance-auditor': (52, 82),
    'data-privacy-officer': (62, 82),
    'document-generator': (26, 62),
    'frontend-developer': (38, 16),
    'ux-researcher': (43, 16),
    'software-architect': (48, 16),
    'backend-architect': (53, 16),
}

BUSINESSES = {
    'appointment-setting': ROOT / 'businesses/appointment-setting',
    'lead-generation-broker': ROOT / 'businesses/lead-generation-broker',
    'recruiting': ROOT / 'businesses/recruiting',
}

BUILDING_DEFAULTS = {
    'agent_barracks': {
        'name': 'Agent Barracks',
        'level': 1,
        'action': 'refresh_worker_roster',
        'actionLabel': 'Refresh worker roster',
        'assignedAgent': 'Chief of Staff',
        'role': 'Worker registry, Agency Agents sync, and visible NPC staffing.',
        'safeNote': 'Reads local Agency Agents TOML files and spawned-worker registry only; no outreach or external actions.',
        'currentTask': 'Ready to reconcile Agency Agents personas and spawned cron workers into visible farm NPCs.',
    },
    'revenue_vault': {
        'name': 'Bank / Model-Cost Building',
        'level': 1,
        'action': 'review_model_costs',
        'actionLabel': 'Review model costs',
        'assignedAgent': 'Finance Tracker',
        'role': 'Revenue targets, gold, and model-cost discipline.',
        'safeNote': 'Reads local revenue/target files only; does not spend money.',
        'currentTask': 'Ready to compare tracked revenue against monthly targets and model-cost discipline.',
    },
    'outreach_tower': {
        'name': 'Outreach Office',
        'level': 1,
        'action': 'prepare_outreach',
        'actionLabel': 'Prepare safe outreach batch',
        'assignedAgent': 'Sales Outreach',
        'role': 'Compliant lead batch and outreach preparation.',
        'safeNote': 'Prepares drafts and logs only; no cold emails or calls are sent.',
        'currentTask': 'Ready to queue lead criteria, subject lines, first lines, and opt-out-safe copy.',
    },
    'operations_foundation': {
        'name': 'Fulfillment Workshop',
        'level': 1,
        'action': 'update_fulfillment_sop',
        'actionLabel': 'Harden fulfillment SOP',
        'assignedAgent': 'Operations Manager',
        'role': 'Delivery SOPs, QA, and automation handoffs.',
        'safeNote': 'Updates task/quest state only until a human approves external client delivery.',
        'currentTask': 'Ready to queue an SOP hardening task with inputs, QA checks, outputs, and handoffs.',
    },
    'client_hall': {
        'name': 'Client Success Hall',
        'level': 1,
        'action': 'client_success_check',
        'actionLabel': 'Prepare retention loop',
        'assignedAgent': 'Support Responder',
        'role': 'Retention, support, and reporting workflows.',
        'safeNote': 'Creates internal follow-up/reporting tasks only; no customer messages are sent.',
        'currentTask': 'Ready to queue a client-health, support follow-up, and reporting cadence review.',
    },
    'market': {
        'name': 'Market Board',
        'level': 1,
        'action': 'queue_market_research',
        'actionLabel': 'Scout zero-cost opportunity',
        'assignedAgent': 'Offer & Lead Gen Strategist',
        'role': 'Business purchase / opportunity board.',
        'safeNote': 'Uses public/free research only; no paid tools, scraping bypass, or outreach.',
        'currentTask': 'Ready to queue one low-cost recurring-revenue opportunity scan.',
    },
}

class RPGHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress default access logging
        pass

    def _send_json(self, obj, status=200):
        payload = json.dumps(obj, indent=2).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(payload)

    def _load_state(self):
        if GAME_STATE.exists():
            with open(GAME_STATE, 'r') as f:
                return json.load(f)
        return {
            "buildings": {},
            "agents": [],
            "quests": [],
            "resources": {},
            "timestamp": datetime.utcnow().isoformat() + 'Z'
        }

    def _save_state(self, state):
        state['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        with open(GAME_STATE, 'w') as f:
            json.dump(state, f, indent=2)
        return state

    def _load_agency_personas(self):
        personas = []
        if not AGENCY_AGENT_DIR.exists():
            return personas
        for slug, task in BUSINESS_AGENT_SLUGS.items():
            path = AGENCY_AGENT_DIR / f'{slug}.toml'
            if not path.exists():
                continue
            try:
                data = tomllib.loads(path.read_text())
            except Exception:
                continue
            x, y = AGENT_POSITIONS.get(slug, (50, 50))
            desc = str(data.get('description') or '').strip()
            personas.append({
                'id': f'agency:{slug}',
                'name': str(data.get('name') or slug.replace('-', ' ').title())[:120],
                'role': desc[:95] or 'Agency Agent worker',
                'status': 'working' if slug not in ('finance-tracker', 'support-responder', 'legal-compliance-checker') else 'watching',
                'x': x,
                'y': y,
                'persona_source': str(path),
                'personality': desc,
                'current_task': task,
                'agency_slug': slug,
                'emoji': self._emoji_for_slug(slug),
            })
        return personas

    def _emoji_for_slug(self, slug):
        if 'sales' in slug or 'lead' in slug or 'growth' in slug or 'seo' in slug or 'content' in slug or 'outbound' in slug or 'discovery' in slug or 'deal' in slug or 'pipeline' in slug or 'proposal' in slug or 'account' in slug:
            return '🎯'
        if 'citation' in slug or 'aeo' in slug or 'agentic-search' in slug:
            return '🧭'
        if 'governance' in slug:
            return '🛡️'
        if 'finance' in slug or 'pricing' in slug or 'chief-financial' in slug:
            return '💰'
        if 'support' in slug or 'customer-success' in slug:
            return '🎧'
        if 'legal' in slug or 'compliance' in slug or 'privacy' in slug:
            return '⚖️'
        if 'document' in slug:
            return '📄'
        if 'frontend' in slug or 'ux' in slug:
            return '🎮'
        if 'architect' in slug or 'backend' in slug:
            return '🏗️'
        if 'strategist' in slug and 'business' in slug:
            return '🧠'
        if 'recruit' in slug:
            return '🧲'
        if 'api' in slug or 'tester' in slug or 'test' in slug or 'accessibility' in slug or 'performance' in slug:
            return '🧪'
        if 'reality' in slug or 'evidence' in slug:
            return '🔎'
        if 'analytics' in slug or 'reporter' in slug or 'summary' in slug:
            return '📊'
        if 'operations' in slug or 'workflow' in slug:
            return '⚙️'
        if 'tool' in slug:
            return '🧰'
        return '🧭'

    def _ensure_building_defaults(self, state):
        """Expose every business station in live state with its safe action contract."""
        buildings = state.setdefault('buildings', {})
        for key, defaults in BUILDING_DEFAULTS.items():
            current = buildings.setdefault(key, {})
            for field, value in defaults.items():
                current.setdefault(field, value)
        return state

    def _sync_agency_agents(self, state):
        """Merge selected Agency Agents TOML personas into live state without deleting spawned workers."""
        agents = state.setdefault('agents', [])
        existing_by_name = {a.get('name'): a for a in agents if a.get('name')}
        existing_by_id = {a.get('id'): a for a in agents if a.get('id')}
        for persona in self._load_agency_personas():
            current = existing_by_id.get(persona['id']) or existing_by_name.get(persona['name'])
            if current:
                preserved = {
                    'last_message': current.get('last_message'),
                    'last_seen': current.get('last_seen'),
                    'dialogue': current.get('dialogue'),
                }
                current.update(persona)
                for key, val in preserved.items():
                    if val:
                        current[key] = val
            else:
                agents.append(persona)
        state['agents'] = agents
        state.setdefault('agent_registry', {})['agency_persona_count'] = len(self._load_agency_personas())
        state['agent_registry']['agency_source'] = str(AGENCY_AGENT_DIR)
        return state

    def _persona_reply(self, agent, message):
        name = agent.get('name', 'Agent')
        task = agent.get('current_task') or 'the current company mission'
        desc = agent.get('personality') or agent.get('role') or 'I keep the business moving.'
        lower = message.lower()
        if any(word in lower for word in ('status', 'update', 'working on', 'doing')):
            intent = f'Status: I am working on {task}'
        elif any(word in lower for word in ('lead', 'outreach', 'email', 'call')):
            intent = 'Outbound note: I can prepare safe batches, scripts, and logs, but I will not send cold emails or place AI/prerecorded calls from the game.'
        elif any(word in lower for word in ('revenue', 'price', 'gold', 'cost')):
            intent = 'Revenue note: I will tie recommendations to real revenue files, target progress, and model-cost discipline.'
        else:
            intent = 'Logged. I will use this as operating context for my next visible task update.'
        return f'{name}: {intent} Persona anchor: {desc[:180]}'

    def _count_leads(self, business):
        today = datetime.utcnow().strftime('%Y-%m-%d')
        f = business / 'data' / f'daily_batch_{today}.csv'
        if not f.exists():
            return 0
        with open(f, 'r') as fh:
            return max(0, len(fh.readlines()) - 1)

    def _count_revenue(self):
        total = 0.0
        for b in BUSINESSES.values():
            rev = b / 'data' / 'revenue.csv'
            if rev.exists():
                with open(rev, 'r') as fh:
                    for row in csv.DictReader(fh):
                        amt = row.get('amount', '')
                        if amt:
                            try:
                                total += float(amt)
                            except ValueError:
                                pass
        return int(total)

    def _load_revenue_target(self):
        target = ROOT / 'automation' / 'revenue_target.json'
        if target.exists():
            with open(target, 'r') as f:
                return json.load(f)
        return {
            'appointment-setting': {'monthly_target': 1000, 'months_at_target': 0},
            'lead-generation-broker': {'monthly_target': 1000, 'months_at_target': 0},
            'recruiting': {'monthly_target': 1000, 'months_at_target': 0}
        }

    def _save_revenue_target(self, data):
        with open(ROOT / 'automation' / 'revenue_target.json', 'w') as f:
            json.dump(data, f, indent=2)

    def _append_event(self, event):
        EVENT_LOG.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            **event,
        }
        with open(EVENT_LOG, 'a') as f:
            f.write(json.dumps(payload, ensure_ascii=False) + '\n')
        return payload

    def _load_recent_events(self, limit=25):
        """Read the durable JSONL event log so the farm can recover live events after restarts."""
        if not EVENT_LOG.exists():
            return []
        events = []
        try:
            lines = EVENT_LOG.read_text().splitlines()[-max(1, int(limit)):]
            for line in lines:
                if not line.strip():
                    continue
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(event, dict):
                    events.append(event)
        except OSError:
            return []
        return events[-limit:]

    def _merge_recent_events(self, state, limit=25):
        """Mirror durable JSONL events into game_state.json for frontend quest/event UI."""
        combined = []
        seen = set()
        for event in [*state.get('events', []), *self._load_recent_events(limit)]:
            if not isinstance(event, dict):
                continue
            key = (event.get('timestamp'), event.get('type'), event.get('agent'), event.get('building'), event.get('message'), event.get('action'))
            if key in seen:
                continue
            seen.add(key)
            combined.append(event)
        combined.sort(key=lambda e: str(e.get('timestamp') or ''))
        state['events'] = combined[-limit:]
        return state

    def _upsert_quest(self, state, quest):
        quests = state.setdefault('quests', [])
        existing = next((q for q in quests if q.get('id') == quest['id']), None)
        if existing:
            existing.update(quest)
        else:
            quests.append(quest)
        return quest

    def _station_action(self, state, action, business):
        """Map farm buildings to safe real operating tasks; no external outreach is sent."""
        station_map = {
            'refresh_worker_roster': {
                'building': 'agent_barracks',
                'name': 'Agent Barracks',
                'summary': 'Refreshed the worker roster from local Agency Agents personas and spawned-worker registry so active staff stay visible as NPCs.',
                'quest_id': 'quest-worker-roster-refresh',
                'quest_title': 'Keep Agent Farm worker roster synchronized',
                'owner': 'Chief of Staff',
            },
            'prepare_outreach': {
                'building': 'outreach_tower',
                'name': 'Outreach Office',
                'summary': 'Queued a compliant manual outreach-prep task: lead criteria, subject lines, first lines, and opt-out-safe copy only.',
                'quest_id': 'quest-outreach-prep',
                'quest_title': 'Prepare next safe outreach batch',
                'owner': 'Sales Outreach',
            },
            'review_model_costs': {
                'building': 'revenue_vault',
                'name': 'Bank / Model-Cost Building',
                'summary': 'Queued a finance review: compare revenue, target progress, and model-cost discipline before scaling spend.',
                'quest_id': 'quest-finance-review',
                'quest_title': 'Review gold, revenue targets, and model costs',
                'owner': 'Finance Tracker',
            },
            'queue_market_research': {
                'building': 'market',
                'name': 'Market Board',
                'summary': 'Queued a business opportunity scan using public/free sources; no paid tools, scraping bypass, or outreach.',
                'quest_id': 'quest-market-research',
                'quest_title': 'Scout one low-cost recurring-revenue opportunity',
                'owner': 'Offer & Lead Gen Strategist',
            },
            'update_fulfillment_sop': {
                'building': 'operations_foundation',
                'name': 'Fulfillment Workshop',
                'summary': 'Queued an SOP hardening task: inputs, QA checklist, output format, and handoff notes for repeatable delivery.',
                'quest_id': 'quest-fulfillment-sop',
                'quest_title': 'Harden fulfillment SOP and QA checklist',
                'owner': 'Operations Manager',
            },
            'client_success_check': {
                'building': 'client_hall',
                'name': 'Client Success Hall',
                'summary': 'Queued a retention check: support follow-up loop, client health notes, and reporting cadence.',
                'quest_id': 'quest-client-success',
                'quest_title': 'Prepare client success retention loop',
                'owner': 'Support Responder',
            },
        }
        spec = station_map.get(action)
        if not spec:
            return None
        if action == 'refresh_worker_roster':
            self._sync_agency_agents(state)
        now = datetime.utcnow().isoformat() + 'Z'
        building = state.setdefault('buildings', {}).setdefault(spec['building'], {'name': spec['name'], 'level': 1})
        building['lastAction'] = action
        building['lastActionAt'] = now
        building['currentTask'] = spec['summary']
        building['assignedAgent'] = spec['owner']
        event = self._append_event({
            'type': 'building_action',
            'building': spec['name'],
            'action': action,
            'business': business,
            'message': spec['summary'],
            'source': 'rpg_building',
        })
        state.setdefault('events', [])
        state['events'] = (state['events'] + [event])[-25:]
        self._upsert_quest(state, {
            'id': spec['quest_id'],
            'title': spec['quest_title'],
            'status': 'active',
            'business': business,
            'assigned_agent': spec['owner'],
            'source': 'rpg_building',
            'updated_at': now,
            'next_step': spec['summary'],
        })
        return event

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        if path in ('/api/state', '/game_state.json'):
            state = self._load_state()
            state = self._ensure_building_defaults(state)
            state = self._sync_agency_agents(state)
            state = self._merge_recent_events(state)
            # Recompute resource totals from real files and persist the live backend-backed view
            # so the UI, game_state.json, and later cron runs stay in sync.
            resources = state.setdefault('resources', {})
            total_leads = sum(self._count_leads(b) for b in BUSINESSES.values())
            total_revenue = self._count_revenue()
            resources['leads'] = total_leads
            resources['gold'] = total_revenue
            state['resources'] = resources
            state = self._save_state(state)
            self._send_json(state)
            return

        if path == '/api/events':
            state = self._load_state()
            state = self._merge_recent_events(state)
            state = self._save_state(state)
            self._send_json({'events': state.get('events', [])})
            return

        if path == '/api/quests':
            state = self._load_state()
            self._send_json({'quests': state.get('quests', [])})
            return

        if path == '/api/agents':
            state = self._load_state()
            state = self._sync_agency_agents(state)
            self._send_json({'agents': state.get('agents', [])})
            return

        if path == '/api/sync_agents':
            state = self._load_state()
            state = self._sync_agency_agents(state)
            self._save_state(state)
            self._send_json({'success': True, 'agents': len(state.get('agents', [])), 'registry': state.get('agent_registry', {})})
            return

        if path == '/api/revenue':
            revenue_data = self._load_revenue_target()
            monthly = self._count_revenue()
            self._send_json({
                'revenue': monthly,
                'targets': revenue_data
            })
            return

        if path == '/api/buildings':
            state = self._load_state()
            state = self._ensure_building_defaults(state)
            self._send_json({'buildings': state.get('buildings', {})})
            return

        if path == '/api/health':
            self._send_json({
                'status': 'ok',
                'businesses': list(BUSINESSES.keys()),
                'timestamp': datetime.utcnow().isoformat() + 'Z'
            })
            return

        # Static file fallback: public HTML plus local, pre-vetted RPG assets.
        if path.startswith('/assets/'):
            base_dir = ROOT / 'rpg-command-center/engine/assets'
            rel_path = path.removeprefix('/assets/')
        else:
            base_dir = ROOT / 'rpg-command-center/engine/public'
            rel_path = path.lstrip('/')
        file_path = (base_dir / rel_path).resolve()
        try:
            file_path.relative_to(base_dir.resolve())
        except ValueError:
            self._send_json({'error': 'invalid asset path'}, 403)
            return
        if file_path.exists() and file_path.is_file():
            with open(file_path, 'rb') as f:
                data = f.read()
            self.send_response(200)
            if file_path.suffix == '.html':
                ctype = 'text/html; charset=utf-8'
            elif file_path.suffix == '.js':
                ctype = 'application/javascript; charset=utf-8'
            elif file_path.suffix == '.json':
                ctype = 'application/json; charset=utf-8'
            elif file_path.suffix == '.png':
                ctype = 'image/png'
            elif file_path.suffix in ('.jpg', '.jpeg'):
                ctype = 'image/jpeg'
            else:
                ctype = 'application/octet-stream'
            self.send_header('Content-Type', ctype)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(data)
            return

        self._send_json({'error': 'not found'}, 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        if path == '/api/action':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length) or '{}') if length else {}
            requested_action = str(body.get('action', '')).strip()
            action_aliases = {
                # Frontend/dialog contract keywords. Keep these stable for game UI buttons
                # while routing them to the existing safe backend actions.
                'revenue': 'collect_revenue',
                'outreach': 'prepare_outreach',
                'reward': 'grant_reward',
            }
            action = action_aliases.get(requested_action, requested_action)
            business = body.get('business', 'appointment-setting')
            amount = float(body.get('amount', 0))

            state = self._load_state()
            state = self._ensure_building_defaults(state)
            buildings = state.setdefault('buildings', {})
            event = None

            if action == 'generate_batch':
                target = BUSINESSES.get(business)
                if target:
                    script = target / 'scripts' / 'daily_batch_runner.py'
                    if script.exists():
                        subprocess.run(['python3', str(script)], capture_output=True)

            if action == 'collect_revenue':
                key = business if business in BUSINESSES else 'appointment-setting'
                rev_data = self._load_revenue_target()
                current = {'monthly_target': 1000, 'months_at_target': 0}
                current.update(rev_data.get(key, current))

                monthly_rev = self._count_revenue()
                if monthly_rev >= current['monthly_target']:
                    current['months_at_target'] += 1
                else:
                    current['months_at_target'] = 0

                rev_data[key] = current
                self._save_revenue_target(rev_data)
                event = self._append_event({
                    'type': 'revenue_check',
                    'building': 'Bank / Model-Cost Building',
                    'action': action,
                    'business': key,
                    'message': f'Revenue check complete: ${monthly_rev} tracked against ${current["monthly_target"]} monthly target; months at target = {current["months_at_target"]}.',
                    'source': 'rpg_revenue',
                })
                state.setdefault('events', [])
                state['events'] = (state['events'] + [event])[-25:]
                self._upsert_quest(state, {
                    'id': 'quest-finance-review',
                    'title': 'Review gold, revenue targets, and model costs',
                    'status': 'active',
                    'business': key,
                    'assigned_agent': 'Finance Tracker',
                    'source': 'rpg_revenue',
                    'updated_at': event['timestamp'],
                    'next_step': event['message'],
                })

            if action == 'grant_reward':
                resources = state.setdefault('resources', {})
                resources['verified_work_xp'] = resources.get('verified_work_xp', 0) + int(amount or 25)
                state['resources'] = resources
                event = self._append_event({
                    'type': 'reward_granted',
                    'action': action,
                    'business': business,
                    'message': f'Granted {int(amount or 25)} verified-work XP for completed/verified work. This is RPG progress only; gold remains tied to real revenue files.',
                    'source': 'rpg_reward',
                })
                state.setdefault('events', [])
                state['events'] = (state['events'] + [event])[-25:]

            if action == 'sync_agents':
                before = len(state.get('agents', []))
                state = self._sync_agency_agents(state)
                after = len(state.get('agents', []))
                event = self._append_event({
                    'type': 'agent_roster_sync',
                    'action': action,
                    'business': business,
                    'message': f'Synced Agency Agents persona roster into the farm: {after} visible workers ({max(0, after-before)} newly added).',
                    'source': 'rpg_agent_registry',
                })
                state.setdefault('events', [])
                state['events'] = (state['events'] + [event])[-25:]

            station_event = self._station_action(state, action, business)
            if station_event:
                event = station_event

            if action == 'agent_message':
                agent_name = str(body.get('agent', 'Unknown Agent'))[:120]
                message = str(body.get('message', '')).strip()[:2000]
                if not message:
                    self._send_json({'success': False, 'error': 'message required'}, 400)
                    return
                agent = next((a for a in state.get('agents', []) if a.get('name') == agent_name), {})
                event = self._append_event({
                    'type': 'agent_message',
                    'agent': agent_name,
                    'role': agent.get('role', body.get('role', 'Worker')),
                    'message': message,
                    'reply': self._persona_reply(agent, message),
                    'source': 'rpg_dialog',
                })
                state.setdefault('events', [])
                state['events'] = (state['events'] + [event])[-25:]
                if agent:
                    agent['last_message'] = message
                    agent['last_seen'] = event['timestamp']

            state = self._save_state(state)
            self._send_json({
                'success': True,
                'state': state,
                'action': action,
                'business': business,
                'event': event,
                'reply': event.get('reply') if action == 'agent_message' and event else None
            })
            return

        self._send_json({'error': 'not found'}, 404)

def run_server(port=7457):
    server = HTTPServer(('0.0.0.0', port), RPGHandler)
    print(f'RPG Command Center backend running on http://127.0.0.1:{port}')
    print(f'Game state: {GAME_STATE}')
    server.serve_forever()

if __name__ == '__main__':
    run_server()
