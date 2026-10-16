"""Acquire only the approved essay list using the nature-downloader provider."""
import concurrent.futures
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
provider = Path('C:/Users/ME/.codex/skills/nature-downloader/scripts/batch_download.mjs')
records = json.loads((root / 'essay-additions-2026-10-12.json').read_text(encoding='utf-8'))
urls = {
    'leopold-mountain': 'https://eowilsonfoundation.org/wp-content/uploads/2023/10/Thinking-Like-a-Mountain-Essay.pdf',
    'dillard-weasels': 'https://openlab.citytech.cuny.edu/fyw-oer-eng-1101-rhetorical-modes/files/2017/12/6.1-Descriptive-Mode-Dillard-Questions.pdf',
    'borges-wilkins': 'https://sites.evergreen.edu/politicalshakespeares/wp-content/uploads/sites/226/2015/12/Borges-The-Analytical-Language-of-JW.pdf',
    'sacks-colorblind': 'https://www.csh.rit.edu/~oguns/school/psychology/Articles/colorblindpainter.pdf',
    'woolf-moth': 'https://docenti.unimc.it/sharifah.alatas/teaching/2019/21609/files/Woolf_DeathoftheMoth.pdf',
    'schelling-segregation': 'https://acoustique.ec-lyon.fr/chaos/Schelling71.pdf',
    'boulding-spaceship': 'https://arachnid.biosci.utexas.edu/courses/THOC/Readings/Boulding_SpaceshipEarth.pdf',
    'flexner-useless': 'https://www.ias.edu/ideas/usefulness-useless-knowledge',
    'russell-idleness': 'https://humanum.arts.cuhk.edu.hk/humftp/E-text/Russell/praise.htm',
    'thurber-bed': 'https://www.newyorker.com/magazine/1933/07/08/my-life-and-hard-times-i-the-night-the-bed-fell',
}

def acquire(record):
    target = root / 'originals-2026-10-12' / record['id']
    if (target / 'manifest.json').exists():
        return {'id': record['id'], 'cached': True, 'manifest': str(target / 'manifest.json')}
    args = ['node', str(provider), '--pdf-url', urls[record['id']], '--title', record['title'], '--language', 'en', '--open-access', '--no-si', '--out', str(target)]
    result = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
    try:
        output = json.loads(result.stdout)
    except ValueError:
        output = {'exit_code': result.returncode, 'error': (result.stderr or result.stdout)[-250:]}
    return {'id': record['id'], 'result': output}

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    tasks = {pool.submit(acquire, record): record for record in records if record['id'] in urls}
    for future in concurrent.futures.as_completed(tasks):
        try:
            result = future.result()
        except Exception as exc:
            result = {'id': tasks[future]['id'], 'error': str(exc)}
        results.append(result)
        print(json.dumps(result, ensure_ascii=False), flush=True)
(root / 'download-results-2026-10-12.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
