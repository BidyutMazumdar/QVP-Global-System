# QSSI™ / QVP™ GLOBAL SYSTEM
## V11 INTERNATIONAL THIRD-PARTY LICENSE & DEPENDENCY GOVERNANCE REGISTER

**Document:** `THIRD_PARTY_LICENSES.md`  
**Framework:** QSSI™ / QVP™ Global System  
**Release Line:** V11  
**Governance Domain:** Third-Party Intellectual Property, Software, Data, Database, Documentation, API & Dependency Rights  
**Rights Architecture:** Multi-Layer / Rights-Separated  
**Governance Model:** Artifact-Level / Evidence-Based / Traceable / Auditable  
**Status:** ACTIVE / CONTROLLED / TRACEABLE / AUDIT-READY  
**Copyright:** © 2026 B. Mazumdar  
**Related Governance Document:** `RIGHTS_NOTICE.md`  
**License Boundary:** Explicit; no third-party material is presumed to be covered by a QSSI™ / QVP™ public research license

---

## 1. PURPOSE

This document establishes the canonical governance framework for identifying, recording, verifying, attributing, documenting, monitoring, and controlling third-party materials incorporated into, referenced by, distributed with, derived from, or otherwise associated with the QSSI™ / QVP™ Global System V11.

The purpose of this register is to ensure that third-party rights are:

- identified;
- attributed;
- provenance-traceable;
- license-verifiable;
- scope-controlled;
- separated from original QSSI™ / QVP™ intellectual property;
- preserved according to their applicable licensing conditions;
- auditable across releases;
- appropriately documented;
- protected against accidental relicensing;
- protected against unauthorized commercial representation; and
- subject to explicit review where rights status is uncertain.

This document is a **rights-governance, dependency-governance, provenance, attribution, and compliance register**.

It is not a substitute for:

- the original third-party license;
- applicable law;
- contractual terms;
- database-rights analysis;
- data-use terms;
- institutional requirements;
- professional legal advice; or
- jurisdiction-specific rights analysis.

---

# 2. FUNDAMENTAL THIRD-PARTY RIGHTS PRINCIPLE

> **Third-party rights remain governed by their original license, contractual terms, applicable law, and legally enforceable conditions. Distribution within the QSSI™ / QVP™ Global System does not, by itself, alter, replace, expand, restrict, or transfer those rights.**

Accordingly:

- third-party material is not automatically relicensed under CC BY-NC-ND 4.0;
- third-party material is not automatically proprietary QSSI™ / QVP™ intellectual property;
- third-party material must not be represented as QSSI™ / QVP™-owned material merely because it appears in a QSSI™ / QVP™ package;
- third-party license conditions remain applicable within the relevant scope;
- applicable attribution obligations must be preserved;
- redistribution conditions must be respected;
- commercial-use restrictions must be respected;
- database rights must be independently considered where applicable;
- contractual access or use restrictions must not be ignored;
- source provenance must remain traceable; and
- uncertain rights status must be classified as requiring review.

> **Only rights that the relevant rights holder is legally authorized to license may be represented as licensed or otherwise permitted.**

---

# 3. NO AUTOMATIC RELICENSING

The inclusion of a third-party component in any:

- GitHub repository;
- source-code repository;
- research paper;
- technical report;
- dataset;
- computational workflow;
- notebook;
- software package;
- ZIP archive;
- Zenodo record;
- DOI publication;
- documentation package;
- reproducibility package;
- benchmark;
- figure;
- table;
- API integration;
- analytical pipeline;
- dependency tree; or
- institutional archive

does **not** automatically cause that third-party component to become subject to:

- CC BY-NC-ND 4.0;
- a QSSI™ / QVP™ proprietary license;
- a FAIR+D Canon™ license;
- a repository-level license;
- an implied commercial license; or
- any other license not expressly applicable to that component.

> **A repository-level license declaration shall not be interpreted as overriding an applicable third-party license.**

Where a repository contains mixed rights, the rights applicable to individual components shall remain independently identifiable to the extent reasonably practicable.

---

# 4. AUTHORITY AND RIGHTS HIERARCHY

For third-party materials, the following governance hierarchy applies:

1. Applicable law and mandatory statutory requirements
2. Binding contractual obligations and enforceable terms of use
3. Original third-party license or rights declaration
4. Applicable database, data, copyright, trademark, patent, privacy, confidentiality, or other independent rights
5. Explicit artifact-level rights declaration
6. QSSI™ / QVP™ repository governance documentation
7. General repository-level explanatory statements

No lower-level governance document overrides a higher-level legal, contractual, licensing, or rights obligation.

Where a conflict or uncertainty exists, the affected material must be classified as:

`REVIEW_REQUIRED`

until the applicable rights position has been independently verified.

> **This register records and governs rights information; it does not create rights that do not otherwise exist.**

---

# 5. SCOPE

This register may apply to third-party:

- datasets;
- statistical datasets;
- indicators;
- databases;
- database extracts;
- software;
- source code;
- libraries;
- packages;
- frameworks;
- APIs;
- documentation;
- specifications;
- standards;
- ontologies;
- schemas;
- images;
- photographs;
- diagrams;
- maps;
- figures;
- tables;
- text;
- research publications;
- benchmark datasets;
- pretrained models;
- model weights;
- checkpoints;
- machine-learning resources;
- external computational tools;
- external services;
- metadata;
- institutional resources;
- government resources;
- public-sector data;
- archival resources;
- web-derived material;
- machine-readable resources;
- statistical systems; and
- other externally originated intellectual or informational assets.

The scope includes material that is:

- directly distributed;
- embedded;
- bundled;
- imported;
- referenced;
- linked;
- required as a dependency;
- used for computation;
- used for validation;
- used for benchmarking;
- used for training or analysis;
- reproduced in documentation;
- incorporated into figures or tables; or
- otherwise necessary for understanding or reproducing a research artifact.

---

# 6. THIRD-PARTY MATERIAL CLASSIFICATION

Each third-party component should, where reasonably practicable, be classified into one or more of the following categories:

| Class | Description |
|---|---|
| `TP-SOFTWARE` | Third-party software, source code, library, package, framework, or dependency |
| `TP-DATA` | Third-party dataset or data resource |
| `TP-DATABASE` | Third-party database or database-derived material |
| `TP-API` | Third-party API, service, or externally controlled interface |
| `TP-DOCUMENTATION` | Third-party documentation or explanatory material |
| `TP-STANDARD` | External standard, specification, protocol, or technical reference |
| `TP-MEDIA` | Third-party image, figure, diagram, audio, video, or other media |
| `TP-MODEL` | Third-party model, model weights, checkpoint, or computational artifact |
| `TP-TEXT` | Third-party textual material |
| `TP-BENCHMARK` | Third-party benchmark or evaluation resource |
| `TP-METADATA` | Third-party metadata or structured descriptive resource |
| `TP-MIXED` | Material containing multiple third-party rights regimes |
| `TP-UNKNOWN` | Third-party material identified but rights classification not yet verified |

A component may have more than one classification where appropriate.

---

# 7. CANONICAL THIRD-PARTY REGISTER

The following register constitutes the canonical structure for recording third-party materials.

| ID | Component / Material | Type | Provider / Rights Holder | Source / Provenance | Version / Date | License / Rights Basis | Commercial Status | Modification Status | Redistribution Status | Attribution Required | Evidence | Verification Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TP-0001 | `[COMPONENT]` | `[TYPE]` | `[RIGHTS_HOLDER]` | `[SOURCE]` | `[VERSION/DATE]` | `[LICENSE]` | `[STATUS]` | `[STATUS]` | `[STATUS]` | `[YES/NO/CONDITIONAL]` | `[EVIDENCE]` | `REVIEW_REQUIRED` |
| TP-0002 | `[COMPONENT]` | `[TYPE]` | `[RIGHTS_HOLDER]` | `[SOURCE]` | `[VERSION/DATE]` | `[LICENSE]` | `[STATUS]` | `[STATUS]` | `[STATUS]` | `[YES/NO/CONDITIONAL]` | `[EVIDENCE]` | `REVIEW_REQUIRED` |

### Register Status Rule

Placeholder records must not be interpreted as verified third-party licenses.

A row may be changed from:

`REVIEW_REQUIRED`

to:

`VERIFIED`

only after sufficient evidence has been reviewed and recorded.

No component should be represented as `VERIFIED` solely because:

- it is publicly accessible;
- it is downloadable;
- a search engine identifies a license;
- a repository contains a generic license file;
- a dependency manager displays a license label; or
- a third party describes the material as open.

The actual applicable rights position should be established from authoritative or sufficiently reliable evidence.

---

# 8. REQUIRED RIGHTS RECORD

For every significant third-party component, the following information should be recorded where reasonably practicable:

```text
THIRD_PARTY_ID:
COMPONENT_NAME:
COMPONENT_TYPE:
RIGHTS_HOLDER:
ORIGINAL_AUTHOR:
PROVIDER:
SOURCE:
SOURCE_VERSION:
RETRIEVAL_DATE:
LICENSE_NAME:
LICENSE_IDENTIFIER:
LICENSE_VERSION:
LICENSE_SOURCE:
COPYRIGHT_STATUS:
DATABASE_RIGHTS_STATUS:
PATENT_STATUS:
TRADEMARK_STATUS:
COMMERCIAL_USE:
MODIFICATION:
ADAPTATION:
REDISTRIBUTION:
SUBLICENSING:
ATTRIBUTION:
NOTICE_REQUIREMENT:
SHARE_ALIKE_REQUIREMENT:
SOURCE_CODE_REQUIREMENT:
NOTICE_FILE_REQUIREMENT:
ACCESS_RESTRICTIONS:
DATA_USE_RESTRICTIONS:
CONTRACTUAL_RESTRICTIONS:
PRIVACY_REQUIREMENTS:
SECURITY_REQUIREMENTS:
PROVENANCE_REFERENCE:
EVIDENCE_REFERENCE:
INTEGRITY_REFERENCE:
VERIFICATION_STATUS:
REVIEW_DATE:
REVIEWER:
REVIEW_NOTES:


---

9. EVIDENCE STANDARD

Third-party rights classification should be evidence-based.

Acceptable evidence may include, where applicable:

official license text;

official provider licensing page;

official terms of use;

official dataset documentation;

official repository license file;

official API terms;

official data-use agreement;

authoritative institutional documentation;

copyright or rights statement;

source metadata;

archival metadata;

documented contractual authorization;

documented permission from the rights holder; or

other sufficiently reliable rights evidence.


Evidence should be preserved through a traceable reference wherever reasonably practicable.

Evidence may include:

EVIDENCE_TYPE:
EVIDENCE_SOURCE:
EVIDENCE_DATE:
EVIDENCE_VERSION:
EVIDENCE_REFERENCE:
EVIDENCE_HASH:
EVIDENCE_NOTES:

Where the evidence cannot be independently verified, the component should remain:

REVIEW_REQUIRED

or:

UNKNOWN

as appropriate.


---

10. VERIFICATION STATUS MODEL

The following verification states are recommended:

Status	Meaning

VERIFIED	Rights position reviewed and sufficiently evidenced
CONDITIONALLY_VERIFIED	Rights position verified subject to specified conditions
REVIEW_REQUIRED	Rights position requires additional review
UNKNOWN	Rights position cannot currently be established
CONFLICT_DETECTED	Conflicting rights information has been identified
EXPIRED_OR_CHANGED	Previously relied-upon rights information may no longer apply
WITHDRAWN	Permission or authorization has been withdrawn
NOT_APPLICABLE	Third-party rights classification does not require the relevant field


A VERIFIED status does not mean that every possible legal issue has been resolved.

It means only that the recorded rights position has been reviewed against the available evidence to the governance standard applicable to the release.


---

11. LICENSE IDENTIFICATION

Where a third-party component is licensed, the register should record, where available:

license name;

license identifier;

license version;

license source;

license date;

applicable scope;

copyright notice requirements;

attribution requirements;

modification requirements;

redistribution requirements;

commercial-use conditions;

notice requirements;

source-code obligations;

share-alike requirements;

patent provisions;

trademark limitations;

warranty disclaimers; and

other material conditions.


License identifiers should be recorded accurately and should not be inferred solely from a similar license name.

Where the license cannot be confidently identified:

LICENSE_STATUS = REVIEW_REQUIRED

should be used.


---

12. SOFTWARE DEPENDENCY GOVERNANCE

Third-party software dependencies should be governed independently from original QSSI™ / QVP™ source code.

For each significant software dependency, where reasonably practicable, record:

DEPENDENCY_NAME:
PACKAGE_ECOSYSTEM:
PACKAGE_IDENTIFIER:
VERSION:
SOURCE_REPOSITORY:
UPSTREAM_PROVIDER:
RIGHTS_HOLDER:
LICENSE:
LICENSE_VERSION:
DEPENDENCY_SCOPE:
DIRECT_OR_TRANSITIVE:
COMMERCIAL_USE:
MODIFICATION:
REDISTRIBUTION:
NOTICE_REQUIREMENT:
SOURCE_CODE_REQUIREMENT:
PATENT_TERMS:
SECURITY_STATUS:
VULNERABILITY_REVIEW:
INTEGRITY_REFERENCE:
VERIFICATION_STATUS:

A third-party software dependency does not become QSSI™ / QVP™ proprietary software merely because it is:

imported;

executed;

packaged;

bundled;

called by;

integrated into;

referenced by; or

distributed alongside


an original QSSI™ / QVP™ implementation.

Conversely, QSSI™ / QVP™ proprietary material does not automatically inherit the license of a dependency merely because the dependency is used within the same software environment.

License compatibility must therefore be assessed at the relevant component and distribution boundary.


---

13. DATA GOVERNANCE

Third-party datasets require rights analysis beyond ordinary copyright analysis where applicable.

For each significant dataset, consider:

copyright status;

database rights;

licensing terms;

data-use restrictions;

redistribution rights;

commercial-use restrictions;

attribution requirements;

update requirements;

access restrictions;

API restrictions;

institutional terms;

jurisdictional restrictions;

privacy requirements;

confidentiality requirements;

security requirements;

provenance;

collection methodology; and

downstream-use conditions.


A dataset being publicly accessible does not necessarily mean that unrestricted redistribution, commercial use, extraction, republication, or database reuse is permitted.


---

14. DATABASE RIGHTS

Where third-party databases or substantial database contents are used, the governance record should independently consider applicable database rights.

The following fields should be recorded where relevant:

DATABASE_NAME:
DATABASE_RIGHTS_HOLDER:
DATABASE_RIGHTS_BASIS:
DATABASE_LICENSE:
DATABASE_VERSION:
DATABASE_SCOPE:
EXTRACTION_RIGHTS:
REUTILIZATION_RIGHTS:
SUBSTANTIAL_PART_USE:
NON_SUBSTANTIAL_USE:
REDISTRIBUTION:
COMMERCIAL_USE:
ATTRIBUTION:
DATABASE_PROVENANCE:
VERIFICATION_STATUS:

Database rights, where applicable, should not be assumed to be identical to copyright rights.

A database may therefore require separate analysis even where individual data points or factual information may have different legal treatment.


---

15. API AND EXTERNAL SERVICE GOVERNANCE

Third-party APIs and externally controlled services may be subject to:

API terms of service;

usage limits;

authentication requirements;

data-retention policies;

access restrictions;

commercial-use restrictions;

redistribution restrictions;

attribution requirements;

caching restrictions;

storage restrictions;

geographic limitations;

security requirements;

contractual conditions; and

service-specific licensing terms.


API access does not automatically grant ownership of:

API responses;

underlying datasets;

proprietary algorithms;

service infrastructure;

trademarks;

documentation;

software;

or other provider-owned materials.


API-dependent artifacts should record the relevant provider and applicable terms wherever reasonably practicable.


---

16. THIRD-PARTY DOCUMENTATION AND TEXT

Third-party documentation, publications, technical descriptions, standards, specifications, and textual materials remain subject to their applicable rights.

Where excerpts, quotations, figures, tables, or other material are used, the release should preserve applicable:

attribution;

citation;

copyright notices;

license notices;

permission statements;

source references; and

usage limitations.


No third-party textual material should be represented as original QSSI™ / QVP™ authorship merely because it is reproduced or referenced in a research package.


---

17. THIRD-PARTY MEDIA

Third-party:

photographs;

diagrams;

figures;

maps;

icons;

logos;

illustrations;

audio;

video; and

other media


must be separately assessed where applicable.

Particular attention should be given to:

copyright;

trademark;

publicity or personality rights where applicable;

licensing scope;

modification restrictions;

attribution;

commercial-use restrictions;

editorial-use restrictions;

geographic limitations; and

embedding or redistribution restrictions.


A third-party logo or trademark appearing in research material does not imply endorsement, sponsorship, certification, or affiliation.


---

18. STANDARDS, SPECIFICATIONS, AND TECHNICAL REFERENCES

External standards and specifications may be subject to distinct rights conditions.

The use of a standard for technical reference does not automatically grant rights to:

reproduce the complete standard;

redistribute protected text;

reproduce protected figures;

reproduce proprietary specifications;

claim certification;

claim official conformity; or

represent independent implementation as an officially certified implementation.


Where standards are referenced, the register should distinguish:

REFERENCE_ONLY

from:

CONTENT_REPRODUCED

and:

IMPLEMENTATION_DEPENDENCY

as appropriate.


---

19. ATTRIBUTION GOVERNANCE

Where attribution is required, the applicable attribution should be preserved in a manner reasonably appropriate to the medium.

Attribution records may include:

ATTRIBUTION_REQUIRED:
ATTRIBUTION_TEXT:
AUTHOR:
RIGHTS_HOLDER:
SOURCE:
LICENSE:
LICENSE_VERSION:
DOI:
VERSION:
ACCESS_DATE:
ADDITIONAL_NOTICE:

Attribution should not:

imply endorsement;

imply certification;

imply authorship where none exists;

imply ownership transfer; or

suggest that third-party material is original QSSI™ / QVP™ intellectual property.



---

20. NOTICE PRESERVATION

Where a third-party license requires preservation of copyright notices, license notices, disclaimers, or other legal notices, those notices should be retained in the relevant distribution where applicable.

The release process should not intentionally remove, obscure, or replace required third-party notices.

Where technically necessary, notices may be consolidated into an appropriate third-party notices file provided that the applicable license conditions permit that method of presentation.


---

21. PROVENANCE REQUIREMENT

Third-party material should remain traceable to its source wherever reasonably practicable.

Minimum provenance information should include:

SOURCE_PROVIDER:
SOURCE_NAME:
SOURCE_LOCATION:
SOURCE_VERSION:
SOURCE_DATE:
RETRIEVAL_DATE:
SOURCE_IDENTIFIER:
DOI_OR_IDENTIFIER:
PROVENANCE_REFERENCE:

For data-derived artifacts, provenance should additionally record, where applicable:

SOURCE_DATASET:
SOURCE_TABLE:
SOURCE_INDICATOR:
SOURCE_VARIABLE:
SOURCE_YEAR:
TRANSFORMATION:
FILTERING:
NORMALIZATION:
HARMONIZATION:
DERIVATION:
PROCESSING_REFERENCE:

Provenance records should distinguish between:

original source material;

transformed material;

derived material;

aggregated material;

harmonized material; and

independently created QSSI™ / QVP™ material.



---

22. DERIVED AND TRANSFORMED MATERIAL

Transformation of third-party material does not automatically eliminate the underlying third-party rights.

Where a QSSI™ / QVP™ artifact is derived from third-party material, the governance record should identify:

original source;

transformation performed;

extent of transformation;

resulting artifact;

applicable third-party rights;

applicable QSSI™ / QVP™ rights;

attribution requirements; and

redistribution conditions.


A derived artifact may therefore have:

MIXED_RIGHTS

status.

> Transformation, normalization, aggregation, harmonization, analysis, or computational processing does not by itself establish unrestricted ownership or unrestricted licensing rights over the underlying third-party material.




---

23. MIXED-RIGHTS GOVERNANCE

Where an artifact contains multiple rights regimes, the artifact should be classified:

TP-MIXED

or:

MIXED_RIGHTS

as appropriate.

Examples include:

original QSSI™ / QVP™ code plus open-source dependencies;

original research analysis plus third-party datasets;

original figures incorporating third-party maps;

transformed datasets containing externally sourced variables;

documentation containing third-party excerpts;

computational outputs dependent on restricted APIs.


For mixed-rights artifacts:

> Each applicable rights regime must remain identifiable and respected according to its legal and contractual scope.



No single repository-level license should be assumed to override component-level rights.


---

24. LICENSE COMPATIBILITY REVIEW

Before redistribution of a composite artifact, where reasonably practicable, review:

license compatibility;

attribution compatibility;

notice requirements;

redistribution conditions;

modification conditions;

commercial restrictions;

share-alike requirements;

source-code obligations;

patent provisions;

database rights;

contractual restrictions;

API terms;

data-use conditions; and

other material restrictions.


If compatibility cannot be established with reasonable confidence:

REVIEW_REQUIRED

should be assigned.

The absence of a detected conflict should not be represented as a legal determination that no conflict exists.


---

25. COMMERCIAL-USE CONTROL

Third-party commercial-use conditions must be preserved.

Where a third-party component is:

non-commercial only;

commercial-use restricted;

commercially licensed;

subject to separate commercial authorization; or

unclear,


the appropriate status must be recorded explicitly.

No QSSI™ / QVP™ public research license shall be interpreted as expanding a third party's commercial permissions.

Similarly, a third-party permissive license shall not automatically be interpreted as granting commercial rights over separate QSSI™ / QVP™ proprietary components.


---

26. MODIFICATION AND ADAPTATION CONTROL

Where third-party material has modification or adaptation restrictions, the governance record must preserve them.

Possible statuses include:

PERMITTED
CONDITIONALLY_PERMITTED
RESTRICTED
PROHIBITED
LICENSE_DEPENDENT
UNKNOWN
REVIEW_REQUIRED

The term "modification" should be interpreted according to the applicable license or legal framework rather than according to an informal repository convention.


---

27. REDISTRIBUTION CONTROL

Redistribution status should be independently recorded.

Possible statuses include:

PERMITTED
CONDITIONALLY_PERMITTED
RESTRICTED
PROHIBITED
LICENSE_DEPENDENT
NOT_APPLICABLE
UNKNOWN
REVIEW_REQUIRED

Public accessibility at the original provider does not automatically establish a right to redistribute the same material in a QSSI™ / QVP™ archive.


---

28. SUBLICENSING CONTROL

Third-party materials must not be sublicensed by QSSI™ / QVP™ unless the applicable rights expressly permit such sublicensing or separate authorization has been obtained.

The following statement applies:

> No third-party material shall be represented as sublicensable merely because it has been incorporated into a QSSI™ / QVP™ artifact.



Where sublicensing rights are uncertain:

SUBLICENSING = REVIEW_REQUIRED


---

29. TRADEMARK GOVERNANCE

Third-party trademarks remain subject to their applicable rights.

Use of a third-party trademark in:

attribution;

compatibility statements;

technical references;

documentation;

scholarly discussion; or

dependency identification


does not necessarily imply:

sponsorship;

endorsement;

certification;

affiliation;

partnership; or

authorization.


Third-party marks should not be modified or represented in a misleading manner.


---

30. PATENT AND NON-COPYRIGHT RIGHTS

Third-party software, technologies, standards, datasets, and systems may involve rights beyond copyright.

Where reasonably practicable, consider:

patents;

patent licenses;

database rights;

design rights;

trademarks;

trade secrets;

confidentiality;

contractual rights; and

other applicable non-copyright rights.


A copyright license should not automatically be interpreted as a complete license to every other category of intellectual-property right.


---

31. PRIVACY AND DATA-PROTECTION GOVERNANCE

Where third-party data contains or may contain personal, sensitive, confidential, or otherwise protected information, additional review may be required.

Relevant considerations may include:

lawful access;

lawful processing;

consent requirements;

data minimization;

anonymization;

pseudonymization;

confidentiality;

retention;

cross-border transfer;

security controls;

contractual restrictions; and

applicable data-protection law.


This register does not itself establish lawful authority to process or redistribute personal data.


---

32. SECURITY AND SUPPLY-CHAIN GOVERNANCE

Third-party software and external computational dependencies should, where relevant, be assessed for:

dependency integrity;

source authenticity;

version identity;

package provenance;

known vulnerabilities;

malicious modification risk;

dependency confusion;

compromised upstream sources;

abandoned dependencies;

integrity verification;

cryptographic hashes; and

supply-chain risk.


Security verification and license verification are separate controls.

A component may be:

LICENSE_VERIFIED

while simultaneously being:

SECURITY_REVIEW_REQUIRED.

Likewise, security verification does not establish licensing authority.


---

33. INTEGRITY AND HASH REFERENCES

Where cryptographic integrity information is available, the register may record:

ARTIFACT_HASH_ALGORITHM:
ARTIFACT_HASH:
SOURCE_HASH:
PACKAGE_HASH:
MANIFEST_REFERENCE:
INTEGRITY_VERIFICATION_DATE:
INTEGRITY_STATUS:

Cryptographic hashes establish artifact identity and integrity.

> A cryptographic hash does not create, transfer, expand, or restrict intellectual-property rights.



Integrity verification and rights verification must therefore remain distinct governance controls.


---

34. EVIDENCE CHAIN

Each significant third-party record should, where reasonably practicable, maintain an evidence chain:

SOURCE
  ↓
PROVENANCE
  ↓
LICENSE / RIGHTS EVIDENCE
  ↓
SCOPE DETERMINATION
  ↓
RIGHTS CLASSIFICATION
  ↓
VERIFICATION
  ↓
RELEASE CONTROL
  ↓
AUDIT RECORD

The evidence chain should be sufficiently clear to allow an independent reviewer to understand:

what material was used;

where it originated;

which rights information was relied upon;

what scope was assessed;

what restrictions were identified; and

why the final governance classification was assigned.



---

35. REVIEW PROCESS

A recommended third-party rights review sequence is:

1. Identify the component.


2. Identify the provider and rights holder where reasonably practicable.


3. Identify the authoritative source.


4. Record version and retrieval date.


5. Identify the applicable license or rights basis.


6. Determine the relevant scope.


7. Review commercial restrictions.


8. Review modification and adaptation restrictions.


9. Review redistribution conditions.


10. Review attribution and notice requirements.


11. Review database and non-copyright rights where applicable.


12. Review contractual or access restrictions.


13. Record provenance.


14. Record evidence.


15. Assign verification status.


16. Record reviewer and review date.


17. Integrate the result into release governance.


18. Re-review when material changes occur.




---

36. CHANGE MANAGEMENT

Third-party rights information may change over time.

Changes may include:

license changes;

provider changes;

ownership changes;

version changes;

terms-of-use changes;

API policy changes;

access restrictions;

commercial restrictions;

withdrawn permissions;

discontinued services;

repository relocation;

dependency replacement; or

newly identified rights conflicts.


A material change should trigger reassessment before the affected component is included in a subsequent controlled release.


---

37. VERSION PINNING

Where practical, software and data dependencies should be version-pinned or otherwise uniquely identified.

Recommended fields include:

COMPONENT_VERSION:
RELEASE_DATE:
COMMIT_ID:
TAG:
PACKAGE_VERSION:
DATASET_VERSION:
CHECKSUM:
DOI:
OTHER_PERSISTENT_IDENTIFIER:

Version identity improves:

reproducibility;

provenance;

auditability;

security review;

license verification; and

release consistency.



---

38. RELEASE-LEVEL THIRD-PARTY AUDIT

Before a controlled release, the third-party register should be reviewed against the actual release contents.

The audit should compare:

DECLARED THIRD-PARTY MATERIAL
        VS.
ACTUAL RELEASE CONTENT

The review should identify:

undeclared dependencies;

missing attribution;

missing license notices;

incompatible licenses;

unidentified datasets;

undocumented APIs;

unexpected media;

unrecorded transitive dependencies;

unresolved rights conflicts;

changed dependency versions; and

stale rights records.



---

39. RELEASE GATE

A release should not be represented as fully third-party-rights-audited where material rights uncertainty remains unresolved.

Recommended release statuses:

Status	Meaning

PASS	Third-party rights governance reviewed and no material unresolved issue identified
PASS_WITH_CONDITIONS	Release may proceed subject to documented conditions
REVIEW_REQUIRED	Material rights issue requires review before release
FAIL	Material rights violation, conflict, or missing authorization identified
NOT_ASSESSED	Third-party rights review has not been completed


A release status should not be upgraded merely because the unresolved issue is inconvenient or difficult to document.


---

40. THIRD-PARTY NOTICE FILE

Where the release contains numerous third-party components, a consolidated notice file may be maintained.

Recommended file:

THIRD_PARTY_NOTICES.md

The notice file may contain:

component name;

provider;

version;

license;

copyright notice;

attribution;

source;

applicable conditions; and

required disclaimers.


The existence of a consolidated notice file does not replace the original third-party licenses.


---

41. MACHINE-READABLE RIGHTS MODEL

A machine-readable representation may use the following structure:

FRAMEWORK: QSSI_QVP_GLOBAL_SYSTEM
RELEASE_LINE: V11
GOVERNANCE_DOMAIN: THIRD_PARTY_RIGHTS
RIGHTS_ARCHITECTURE: MULTI_LAYER / RIGHTS_SEPARATED
THIRD_PARTY_RELICENSING: NOT_PERMITTED_BY_DEFAULT
ORIGINAL_LICENSE_CONTROLS: TRUE
CONTRACTUAL_TERMS_CONTROL: TRUE
APPLICABLE_LAW_CONTROLS: TRUE
DATABASE_RIGHTS_REVIEW: REQUIRED_WHERE_APPLICABLE
COMMERCIAL_RIGHTS: LICENSE_DEPENDENT
MODIFICATION_RIGHTS: LICENSE_DEPENDENT
REDISTRIBUTION_RIGHTS: LICENSE_DEPENDENT
SUBLICENSING: NOT_PERMITTED_UNLESS_AUTHORIZED
ATTRIBUTION: PRESERVE_WHERE_REQUIRED
NOTICE_PRESERVATION: REQUIRED_WHERE_APPLICABLE
PROVENANCE: REQUIRED
EVIDENCE_REFERENCE: REQUIRED_FOR_VERIFICATION
INTEGRITY_REFERENCE: RECOMMENDED
VERIFICATION_STATUS: VERIFIED / CONDITIONAL / REVIEW_REQUIRED / UNKNOWN
MIXED_RIGHTS: SUPPORTED
LICENSE_OVERRIDE: NOT_PERMITTED
THIRD_PARTY_LICENSE_OVERRIDE: NOT_PERMITTED
QSSI_LICENSE_SCOPE: DOES_NOT_AUTOMATICALLY_EXTEND_TO_THIRD_PARTY_MATERIAL
COMMERCIAL_AUTHORIZATION: SEPARATE_WHERE_REQUIRED
GOVERNANCE_STATUS: ACTIVE / CONTROLLED / TRACEABLE / AUDIT-READY


---

42. CANONICAL THIRD-PARTY RECORD TEMPLATE

Each significant third-party component may be represented using the following canonical record:

THIRD_PARTY_ID:
COMPONENT_NAME:
COMPONENT_TYPE:
PACKAGE_OR_DATASET_IDENTIFIER:
RIGHTS_HOLDER:
ORIGINAL_AUTHOR:
PROVIDER:
SOURCE:
SOURCE_VERSION:
SOURCE_RELEASE_DATE:
RETRIEVAL_DATE:

LICENSE_NAME:
LICENSE_IDENTIFIER:
LICENSE_VERSION:
LICENSE_SOURCE:
RIGHTS_BASIS:

COPYRIGHT_STATUS:
DATABASE_RIGHTS_STATUS:
PATENT_STATUS:
TRADEMARK_STATUS:
OTHER_RIGHTS_STATUS:

COMMERCIAL_USE:
MODIFICATION:
ADAPTATION:
REDISTRIBUTION:
SUBLICENSING:

ATTRIBUTION:
NOTICE_REQUIREMENT:
SHARE_ALIKE_REQUIREMENT:
SOURCE_CODE_REQUIREMENT:
NOTICE_FILE_REQUIREMENT:

ACCESS_RESTRICTIONS:
DATA_USE_RESTRICTIONS:
CONTRACTUAL_RESTRICTIONS:
PRIVACY_REQUIREMENTS:
SECURITY_REQUIREMENTS:

PROVENANCE_REFERENCE:
EVIDENCE_REFERENCE:
INTEGRITY_REFERENCE:

DIRECT_OR_TRANSITIVE:
DEPENDENCY_SCOPE:
RELEASE_ARTIFACTS_AFFECTED:

VERIFICATION_STATUS:
REVIEW_DATE:
REVIEWER:
REVIEW_NOTES:
CHANGE_HISTORY:


---

43. COMPLIANCE PRINCIPLES

The following principles govern third-party rights management:

Principle 1 — Identify

Third-party material should be identified wherever reasonably practicable.

Principle 2 — Attribute

Required attribution must be preserved.

Principle 3 — Verify

Rights status should be verified against reliable evidence.

Principle 4 — Separate

Third-party rights must remain separate from QSSI™ / QVP™ proprietary rights.

Principle 5 — Preserve

Applicable notices, licenses, and restrictions must be preserved.

Principle 6 — Trace

Provenance must remain traceable.

Principle 7 — Do Not Override

No repository-level declaration overrides an applicable third-party right.

Principle 8 — Do Not Assume

Public accessibility does not automatically establish unrestricted rights.

Principle 9 — Review Uncertainty

Uncertain rights must be classified as requiring review.

Principle 10 — Audit

Third-party rights should be auditable across controlled releases.


---

44. INCIDENT AND RIGHTS-CONFLICT MANAGEMENT

If a potential third-party rights conflict is identified, the affected material should be treated conservatively.

Recommended immediate controls include:

1. identify the affected component;


2. preserve the current evidence;


3. record the potential conflict;


4. prevent unsupported relicensing claims;


5. determine whether distribution should be restricted;


6. verify the applicable rights;


7. document the resolution;


8. update the register;


9. update affected notices or manifests; and


10. record the resolution in the release audit trail.



Potential incident classifications may include:

LICENSE_CONFLICT
MISSING_ATTRIBUTION
MISSING_NOTICE
UNAUTHORIZED_REDISCLOSURE
UNVERIFIED_RIGHTS
DATABASE_RIGHTS_CONCERN
COMMERCIAL_USE_CONCERN
CONTRACTUAL_RESTRICTION
SOURCE_PROVENANCE_GAP
DEPENDENCY_LICENSE_GAP
RIGHTS_HOLDER_DISPUTE
LICENSE_CHANGE
OTHER


---

45. TAKEDOWN / REPLACEMENT / REMEDIATION

Where a credible rights issue cannot be resolved promptly, the affected material may be:

temporarily withheld;

replaced;

removed from a future release;

redistributed only under appropriate conditions;

isolated from the public package;

reclassified;

subjected to additional authorization; or

otherwise remediated.


Any remediation should preserve the integrity of the audit record.

Removal of a component from a current distribution does not require deletion of historical governance evidence concerning the issue.


---

46. HISTORICAL RELEASE GOVERNANCE

Third-party rights should be evaluated in the context of the release in which the material was distributed.

A later license change does not automatically establish that an earlier distribution was governed by the later license.

Historical records should preserve, where reasonably practicable:

dependency version;

source version;

license version;

evidence available at the time;

retrieval date;

applicable notices;

release identifier; and

governance decision.



---

47. REPRODUCIBILITY AND THIRD-PARTY RIGHTS

Reproducibility may require identifying external datasets, software, APIs, models, or other dependencies.

However:

> Reproducibility requirements do not independently create a right to redistribute third-party material.



Where a third-party dependency cannot lawfully be redistributed, the reproducibility package may instead provide, where legally and technically appropriate:

source identification;

persistent identifiers;

acquisition instructions;

version information;

checksums;

transformation procedures;

metadata;

scripts;

configuration;

documentation; and

other legally permissible reproducibility information.


The goal is to maximize reproducibility within applicable rights boundaries.


---

48. REPOSITORY-LEVEL LICENSE BOUNDARY

The presence of this register does not mean that every item in the repository is third-party material.

Likewise, the presence of a repository-level public research license does not mean that every repository component is governed by that license.

The repository should therefore be interpreted as potentially containing:

ORIGINAL_QSSI_QVP_MATERIAL
+
DESIGNATED_PUBLIC_RESEARCH_MATERIAL
+
PROPRIETARY_MATERIAL
+
THIRD_PARTY_MATERIAL
+
PUBLIC_DOMAIN_MATERIAL
+
MIXED_RIGHTS_MATERIAL

Each category remains subject to its applicable rights framework.


---

49. RELATIONSHIP TO RIGHTS_NOTICE.md

This document operates together with:

RIGHTS_NOTICE.md

The relationship is:

RIGHTS_NOTICE.md
        ↓
Overall rights-separation architecture

THIRD_PARTY_LICENSES.md
        ↓
Third-party dependency and rights governance

LICENSE_SCOPE.md
        ↓
Artifact-level licensing boundaries

LICENSE_MANIFEST.json
        ↓
Machine-readable license declarations

RIGHTS_MATRIX.csv
        ↓
Structured rights classification

ATTRIBUTION.md
        ↓
Attribution and citation governance

No document in this hierarchy should be interpreted as overriding applicable law, binding contractual terms, or the original third-party rights.


---

50. RELATIONSHIP TO QSSI™ / QVP™ PUBLIC RESEARCH LICENSE

Where a QSSI™ / QVP™ artifact is expressly designated as:

CC BY-NC-ND 4.0

that designation applies only to the scope expressly identified for that artifact.

Third-party components embedded in, referenced by, or distributed alongside that artifact remain governed by their respective rights.

Therefore:

> CC BY-NC-ND 4.0 does not automatically extend to third-party components.



Similarly:

> A third-party license does not automatically extend to original QSSI™ / QVP™ proprietary material.




---

51. RIGHTS-SEPARATION RULE

The following rule is canonical:

ORIGINAL QSSI™ / QVP™ MATERIAL
        ≠
THIRD-PARTY MATERIAL

QSSI™ / QVP™ PUBLIC RESEARCH LICENSE
        ≠
THIRD-PARTY LICENSE

THIRD-PARTY LICENSE
        ≠
QSSI™ / QVP™ PROPRIETARY LICENSE

PUBLIC ACCESS
        ≠
COMMERCIAL AUTHORIZATION

REPRODUCIBILITY
        ≠
UNRESTRICTED REDISTRIBUTION

ARCHIVAL PUBLICATION
        ≠
OWNERSHIP TRANSFER


---

52. AUDITABILITY REQUIREMENT

A mature third-party governance record should permit an independent reviewer to answer:

1. What third-party material is present?


2. Who supplied or owns it?


3. Where did it originate?


4. Which version was used?


5. Which license or rights basis applies?


6. What evidence supports that classification?


7. What attribution is required?


8. Is commercial use permitted?


9. Is modification permitted?


10. Is redistribution permitted?


11. Are database rights relevant?


12. Are contractual restrictions relevant?


13. Is the component direct or transitive?


14. Which release artifacts depend on it?


15. When was it last reviewed?


16. Who reviewed it?


17. Is the rights status verified?


18. Has the rights status changed since the previous release?



If these questions cannot reasonably be answered for a material significant dependency, the relevant record should remain appropriately qualified.


---

53. REVIEW FREQUENCY

Third-party rights records should be reviewed:

when a dependency changes version;

when a dataset is updated;

when an API changes terms;

when a provider changes its licensing model;

before major controlled releases;

after a reported rights conflict;

when new third-party material is introduced;

when redistribution scope changes;

when commercial use is contemplated; and

whenever material evidence indicates that the previous rights classification may no longer be accurate.



---

54. GOVERNANCE RECORD RETENTION

Where reasonably practicable, the following should be retained as part of the release governance evidence:

third-party register;

license references;

attribution records;

source references;

dependency manifests;

version information;

evidence references;

review records;

integrity references;

change history;

conflict records;

remediation records; and

release-level audit results.


Historical governance records should not be silently overwritten where doing so would impair auditability.


---

55. PROHIBITED ASSUMPTIONS

The following assumptions are expressly prohibited for governance purposes:

"It is online, therefore it is free to use."

"It is on GitHub, therefore it is open source."

"It is on Zenodo, therefore it is freely redistributable."

"It has a DOI, therefore ownership was transferred."

"It is government data, therefore every use is unrestricted."

"It is publicly downloadable, therefore commercial use is allowed."

"It is a dependency, therefore it is covered by our license."

"It is inside our ZIP, therefore we own it."

"It has no visible copyright notice, therefore it is public domain."

"A repository license overrides a component license."

"A transformed dataset automatically becomes unrestricted."

"Research use automatically permits commercial use."

"Reproducibility automatically permits redistribution."

"A trademark appearing in documentation implies endorsement."


These assumptions must not be used as substitutes for actual rights analysis.


---

56. FINAL THIRD-PARTY RELEASE CHECKLIST

Before final release, verify:

[ ] All material third-party components identified
[ ] Direct dependencies identified
[ ] Material transitive dependencies identified where relevant
[ ] Third-party datasets identified
[ ] Third-party databases identified
[ ] Third-party APIs identified
[ ] Third-party software identified
[ ] Third-party media identified
[ ] Third-party documentation identified
[ ] Applicable licenses identified
[ ] License versions recorded where available
[ ] Rights holders/providers recorded
[ ] Provenance recorded
[ ] Attribution requirements reviewed
[ ] Notice requirements reviewed
[ ] Commercial restrictions reviewed
[ ] Modification restrictions reviewed
[ ] Redistribution restrictions reviewed
[ ] Database rights reviewed where applicable
[ ] Contractual restrictions reviewed where applicable
[ ] Privacy/data-use requirements reviewed where applicable
[ ] Security/supply-chain review performed where applicable
[ ] Evidence references recorded
[ ] Integrity references recorded where available
[ ] Uncertain items marked REVIEW_REQUIRED
[ ] No unsupported relicensing claims
[ ] No third-party license overridden
[ ] No missing mandatory attribution identified
[ ] No unresolved material license conflict
[ ] Third-party notices updated
[ ] Release-level audit completed


---

57. RELEASE DECISION

The final third-party governance decision should be recorded as one of:

THIRD_PARTY_RIGHTS_STATUS: PASS

or:

THIRD_PARTY_RIGHTS_STATUS: PASS_WITH_CONDITIONS

or:

THIRD_PARTY_RIGHTS_STATUS: REVIEW_REQUIRED

or:

THIRD_PARTY_RIGHTS_STATUS: FAIL

A PASS status should be used only where the applicable third-party governance review has been completed to the required release standard.


---

58. CANONICAL GOVERNANCE DECLARATION

> The QSSI™ / QVP™ Global System V11 recognizes and preserves the independent rights of third-party authors, providers, licensors, data custodians, software developers, database rights holders, institutions, and other rights holders. Third-party materials remain governed by their applicable original licenses, contractual terms, provenance conditions, database rights, intellectual-property rights, data-use restrictions, and applicable law. No third-party component is automatically relicensed, transferred, or converted into QSSI™ / QVP™ proprietary or public research material merely because it is incorporated into, referenced by, archived with, or distributed alongside a QSSI™ / QVP™ artifact.



> Where rights are uncertain, the material shall be treated conservatively and classified as requiring review until sufficient evidence establishes the applicable rights position.




---

59. FINAL RIGHTS-GOVERNANCE PRINCIPLE

> IDENTIFY → VERIFY → ATTRIBUTE → SEPARATE → PRESERVE → TRACE → AUDIT



The QSSI™ / QVP™ Global System V11 adopts the following final principle:

> Third-party rights are independent rights. Public research dissemination does not override them. Repository publication does not override them. Archival publication does not override them. A DOI does not override them. A ZIP archive does not override them. A QSSI™ / QVP™ public research license does not override them.



Accordingly:

THIRD-PARTY RIGHTS
        ↓
ORIGINAL LICENSE / CONTRACT / APPLICABLE LAW
        ↓
ARTIFACT-LEVEL RIGHTS DETERMINATION
        ↓
PROVENANCE + EVIDENCE
        ↓
ATTRIBUTION + NOTICE PRESERVATION
        ↓
RELEASE-LEVEL AUDIT
        ↓
CONTROLLED DISTRIBUTION


---

60. OFFICIAL RIGHTS-BOUNDARY STATEMENT

> No QSSI™ / QVP™ repository, publication, dataset package, ZIP archive, DOI record, Zenodo record, GitHub repository, research paper, computational workflow, or reproducibility package shall be interpreted as granting rights over third-party material beyond the rights actually available under the applicable third-party license, contractual authorization, or applicable law.



> Third-party license conditions remain independently enforceable according to their applicable legal and contractual scope.




---

61. COPYRIGHT AND GOVERNANCE NOTICE

© 2026 B. Mazumdar

QSSI™ / QVP™ Global System V11
International Third-Party License & Dependency Governance Register

This document establishes a governance and compliance architecture for third-party rights.

It does not replace:

applicable law;

original third-party licenses;

contractual agreements;

provider terms;

database rights;

data-use restrictions;

institutional requirements;

or professional legal advice.


No statement in this document should be interpreted as creating rights that the relevant rights holder does not possess or cannot lawfully grant.


---

62. FINAL STATUS

DOCUMENT: THIRD_PARTY_LICENSES.md
FRAMEWORK: QSSI™ / QVP™ GLOBAL SYSTEM
RELEASE_LINE: V11

GOVERNANCE_DOMAIN:
THIRD-PARTY INTELLECTUAL PROPERTY / DATA / SOFTWARE / DATABASE /
DOCUMENTATION / API / DEPENDENCY RIGHTS

RIGHTS_ARCHITECTURE:
MULTI-LAYER / RIGHTS-SEPARATED

GOVERNANCE_MODEL:
ARTIFACT-LEVEL / EVIDENCE-BASED / TRACEABLE / AUDITABLE

THIRD_PARTY_RELICENSING:
NOT_PERMITTED_BY_DEFAULT

ORIGINAL_LICENSE_CONTROL:
ACTIVE

CONTRACTUAL_TERMS_CONTROL:
ACTIVE

APPLICABLE_LAW_CONTROL:
ACTIVE

PROVENANCE:
REQUIRED

ATTRIBUTION:
REQUIRED_WHERE_APPLICABLE

NOTICE_PRESERVATION:
REQUIRED_WHERE_APPLICABLE

DATABASE_RIGHTS_REVIEW:
REQUIRED_WHERE_APPLICABLE

COMMERCIAL_RIGHTS:
LICENSE_DEPENDENT

MODIFICATION_RIGHTS:
LICENSE_DEPENDENT

REDISTRIBUTION_RIGHTS:
LICENSE_DEPENDENT

SUBLICENSING:
NOT_PERMITTED_UNLESS_AUTHORIZED

MIXED_RIGHTS:
SUPPORTED

LICENSE_OVERRIDE:
NOT_PERMITTED

THIRD_PARTY_LICENSE_OVERRIDE:
NOT_PERMITTED

UNVERIFIED_RIGHTS:
REVIEW_REQUIRED

INTEGRITY:
TRACEABLE_WHERE_AVAILABLE

AUDITABILITY:
ENABLED

REPRODUCIBILITY:
SUPPORTED_WITHIN_APPLICABLE_RIGHTS

GOVERNANCE_STATUS:
ACTIVE / CONTROLLED / TRACEABLE / AUDIT-READY

RIGHTS_BOUNDARY:
EXPLICIT

FINAL PRINCIPLE:
THIRD-PARTY RIGHTS REMAIN INDEPENDENT AND ARE GOVERNED
BY THEIR APPLICABLE LICENSES, CONTRACTS, PROVENANCE CONDITIONS,
AND APPLICABLE LAW.


---

END OF CANONICAL THIRD-PARTY LICENSE & DEPENDENCY GOVERNANCE REGISTER
