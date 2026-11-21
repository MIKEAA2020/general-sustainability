# Zenodo relation vocabulary — the 34 valid values

`GET https://zenodo.org/api/vocabularies/relationtypes` (checked against the live API).
**`isRelatedTo` does not exist.**

| relation | label |
|---|---|
| `cites` | Cites |
| `compiles` | Compiles |
| `continues` | Continues |
| `describes` | Describes |
| `documents` | Documents |
| `hasmetadata` | Has metadata |
| `haspart` | Has part |
| `hasversion` | Has version |
| `iscitedby` | Is cited by |
| `iscompiledby` | Is compiled by |
| `iscontinuedby` | Is continued by |
| `isderivedfrom` | Is derived from |
| `isdescribedby` | Is described by |
| `isdocumentedby` | Is documented by |
| `isidenticalto` | Is identical to |
| `ismetadatafor` | Is metadata for |
| `isnewversionof` | Is new version of |
| `isobsoletedby` | Is obsoleted by |
| `isoriginalformof` | Is original form of |
| `ispartof` | Is part of |
| `ispreviousversionof` | Is previous version of |
| `ispublishedin` | Is published in |
| `isreferencedby` | Is referenced by |
| `isrequiredby` | Is required by |
| `isreviewedby` | Is reviewed by |
| `issourceof` | Is source of |
| `issupplementedby` | Is supplemented by |
| `issupplementto` | Is supplement to |
| `isvariantformof` | Is variant form of |
| `isversionof` | Is version of |
| `obsoletes` | Obsoletes |
| `references` | References |
| `requires` | Requires |
| `reviews` | Reviews |

## Ones you actually need for this deposit

- `isNewVersionOf` → the previous version of this same record
- `isSupplementTo` → the manuscript/preprint the package supports (use resource type *Preprint*)
- `isIdenticalTo` → the GitHub repository (resource type *Software*)
- `isPreviousVersionOf` / `isVersionOf` → rarely needed; Zenodo's versioning link is automatic
- `cites` → a paper the dataset relies on

**Legacy deposits** written against the old Invenio v1 API do carry `isRelatedTo` — that is a
historical artefact, not a term you can pick in the current UI.
