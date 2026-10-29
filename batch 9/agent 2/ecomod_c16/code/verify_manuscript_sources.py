"""Check transcription and restored author/expository text, not empirical validity."""
from pathlib import Path
import hashlib,json,re
import simulate_budgets as model
ROOT=Path(__file__).resolve().parents[1]

def main():
    text=(ROOT/'ecomod_C16_main.tex').read_text()
    si=(ROOT/'ecomod_C16_SI.tex').read_text()
    record=json.loads((ROOT/'metadata/author_text_integrity.json').read_text())
    checked=[]
    for item in record['segments']:
        start=text.index(item['start']);end=text.index(item['end'],start)
        assert hashlib.sha256(text[start:end].encode()).hexdigest()==item['sha256'],item['name']
        checked.append(item['name'])
    assert record['original_AI_declaration'] in text
    match=re.search(r'\\label\{eq:c13boundsB\}(.*?)\\end\{equation\}',text,re.S)
    assert match
    expression=re.sub(r'\s+','',match.group(1))
    assert r'\frac{b_fL-B}{b_f-u_+}' in expression
    assert 'b_fT' not in expression
    assert '(b_fL-B)/(b_f-u_+)' in re.sub(r'\s+','',si)
    bounds,witnesses,info=model.identification()
    assert info['L']==2.5
    expected=(info['bf']*info['L']-info['B'])/(info['bf']-info['Ups_bounds'][1])
    assert abs(bounds[0]['upper_Ac_ha']-expected)<1e-12
    assert abs(bounds[0]['upper_Ac_ha']-1.6581632653061225)<1e-12
    assert abs(bounds[1]['lower_Ac_ha']-.6060606060606061)<1e-12
    assert abs(bounds[1]['upper_Ac_ha']-.8)<1e-12
    assert abs(bounds[2]['lower_Ac_ha']-.7173601147776184)<1e-12
    assert 'an arbitrarily chosen $0.7$' in text
    assert 'reporting cut of $0.7$' in si
    assert 'a indicator proxy' not in si
    assert 'specification specification' not in si
    output=dict(restored_segments=checked,original_author_AI_declaration_exact=True,
                main_bound_uses_total_area_L=True,SI_bound_uses_total_area_L=True,
                static_implementation_uses_total_area_L=True,example_values_match=True,
                illustrative_reporting_cut_retained=True,
                scope='Source transcription and author-text integrity only; not a comprehensive scientific or empirical validation')
    (ROOT/'metadata/source_verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
