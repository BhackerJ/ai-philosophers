# Traffic archive

`traffic.json` is appended weekly by `.github/workflows/traffic.yml` (GitHub only keeps 14 days of traffic data itself).

- `views` / `clones`: per-day counts and unique visitors
- `snapshots[]`: weekly star/fork counts, top referrers, and top paths

Quick summary:

```bash
python3 -c "import json;d=json.load(open('stats/traffic.json'));print('views',sum(v['count'] for v in d['views'].values()),'clones',sum(v['count'] for v in d['clones'].values()));print(d['snapshots'][-1]['referrers'] if d['snapshots'] else 'no snapshots yet')"
```
