# Benchmark Failure Audit

- Generated: 2026-04-26T20:22:53.352359+00:00
- Results timestamp: 2026-04-26T20:22:45.356281+00:00
- Model: gpt-5.4-nano
- Commit: 430ecea

This report expands failed benchmark rows into a reviewable format with inputs, outputs, and evidence.
Fields are marked as not captured only when the benchmark JSON does not contain them.

## Arm 0 - No Evidence

Failures shown: 51

### 1. AVeriTeC / av_001 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Indian Railways has been completely privatized, and as a result, scores of people working in the Railways would lose their jobs.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** The prompt lists no actual sources or URLs, so there’s nothing to check against the claim about Indian Railways being completely privatized and job losses. Without source text, I can’t determine whether the claim is supported or contradicted.
- **Confidence reason:** No sources/URLs provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "Indian Railways has been completely privatized, and as a result, scores of people working in the Railways would lose their jobs.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_002 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Donald Trump said: "Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children."
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided to verify whether Trump made this statement.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to check against the quoted claim. Without any provided evidence, the claim cannot be supported or contradicted based on the supplied materials.
- **Confidence reason:** No source URLs or content provided
- **Claim verdicts:**
```json
[
  {
    "claim": "Donald Trump said: \"Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_003 - Supported

#### Input
- **Claim:** At independence, Nigeria had a population of 45 million
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No sources were provided to verify Nigeria’s independence-era population.
- **Explanation:** The prompt lists no sources (no URLs or content), so there is nothing to check against the claim that Nigeria had a population of 45 million at independence. Without source material, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "At independence, Nigeria had a population of 45 million",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_004 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** The U.S. surgeon general and the Centers for Disease Control both previously said that ‘masks are not effective in preventing [the] general public from catching coronavirus.’
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be verified.
- **Explanation:** The prompt lists no source URLs or source text. Without any provided material from the U.S. surgeon general or the CDC, it’s impossible to determine whether they previously said that masks are not effective for the general public.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The U.S. surgeon general and the Centers for Disease Control both previously said that ‘masks are not effective in preventing [the] general public from catching coronavirus.’",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_005 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Russia sent medical aid to the US, in the form of medical equipment to help coronavirus patients.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to check against the claim about Russia sending medical aid to the US for coronavirus patients. Without source text, the evidence for or against the claim is unavailable.
- **Confidence reason:** No source URLs or content provided.
- **Claim verdicts:**
```json
[
  {
    "claim": "Russia sent medical aid to the US, in the form of medical equipment to help coronavirus patients.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided to verify South Africa police growth since 2002.
- **Explanation:** The prompt lists no sources (URLs or content), so there is nothing to check against the claim that South Africa’s police force grew by 50% since 2002. Without source material, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_009 - Supported

#### Input
- **Claim:** Today, Nigeria grapple has a population exceeding 200 million.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No sources were provided to verify Nigeria’s population claim.
- **Explanation:** No sources (URLs or content) were included, so there’s nothing to check against the claim that Nigeria’s population exceeds 200 million today. Without source material, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today, Nigeria grapple has a population exceeding 200 million.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_010 - Refuted

#### Input
- **Claim:** UNESCO declared Nadar community as the most ancient race in the world.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No provided sources address UNESCO declaring the Nadar community the most ancient race.
- **Explanation:** No sources were provided, so there is nothing to verify whether UNESCO made such a declaration. Without any source text or URL, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "UNESCO declared Nadar community as the most ancient race in the world.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_011 - Supported

#### Input
- **Claim:** Fact Check: WHO has not approved home remedy for COVID-19, don’t fall for misinformation
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No sources were provided, so the claim can’t be verified.
- **Explanation:** The prompt lists no actual sources or URLs, so there’s nothing to check against the claim about WHO approving home remedies for COVID-19. Without source text, I can’t determine whether WHO has approved any home remedy or whether the claim is accurate.
- **Confidence reason:** No sources/URLs provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fact Check: WHO has not approved home remedy for COVID-19, don’t fall for misinformation",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_013 - Refuted

#### Input
- **Claim:** Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the claim cannot be verified or refuted.
- **Explanation:** The prompt lists no sources or URLs, so there is no evidence to check whether Dr. Ebeneezer made the stated instruction or whether it relates to prostate cancer prevention. Without source text, the claim’s accuracy cannot be evaluated.
- **Confidence reason:** No source URLs or content provided
- **Claim verdicts:**
```json
[
  {
    "claim": "Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. AVeriTeC / av_017 - Supported

#### Input
- **Claim:** Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there’s nothing to verify whether the U.S. lost 300,000 manufacturing jobs due to a China trade war. Without any source material, the claim’s accuracy cannot be supported or contradicted.
- **Confidence reason:** No sources provided to check the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. AVeriTeC / av_019 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided to verify the Twitter warning claim.
- **Explanation:** The prompt includes no source URLs or source content, so there is nothing to check whether Twitter is adding warnings to unedited Biden clip tweets. Without the referenced sources, the claim cannot be supported or contradicted based on provided evidence.
- **Confidence reason:** No sources or URLs provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 13. AVeriTeC / av_020 - Supported

#### Input
- **Claim:** Edo State in Nigeria has a 19% unemployment rate.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No sources were provided, so the 19% unemployment claim can’t be checked.
- **Explanation:** No source URLs or documents were included, so there is nothing to verify whether Edo State’s unemployment rate is 19%. Without any referenced data, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Edo State in Nigeria has a 19% unemployment rate.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 14. AVeriTeC / av_022 - Refuted

#### Input
- **Claim:** The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the donation claim can’t be verified.
- **Explanation:** The prompt lists no sources (no URLs or content) to check whether the Nigerian government is donating $600 million to Joe Biden’s campaign. Without any source text, there’s nothing to support or contradict the claim.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 15. AVeriTeC / av_023 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Even if your mail-in ballot is postmarked prior to the Election day but arrives after the Election day it will be thrown out.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** No source URLs or source text were included, so there’s nothing to verify whether a postmarked-but-late-arriving mail-in ballot is thrown out. Without the referenced sources, the claim’s accuracy cannot be determined.
- **Confidence reason:** No sources provided to assess the claim
- **Claim verdicts:**
```json
[
  {
    "claim": "Even if your mail-in ballot is postmarked prior to the Election day but arrives after the Election day it will be thrown out.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 16. AVeriTeC / av_025 - Refuted

#### Input
- **Claim:** Joe Biden proposed a US wide 2% property tax increase.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided to verify whether Biden proposed a 2% property tax increase.
- **Explanation:** The prompt lists no sources (no URLs or source text) to check the claim. Without any provided evidence, it’s impossible to determine whether Joe Biden proposed a US-wide 2% property tax increase.
- **Confidence reason:** No source material provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Joe Biden proposed a US wide 2% property tax increase.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 17. AVeriTeC / av_026 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** The UK public won’t be able to claim compensation if unlicensed vaccines damage our health.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there’s nothing to check against the claim about UK compensation for damage from unlicensed vaccines. Without any provided evidence, the claim’s accuracy cannot be determined from the supplied materials.
- **Confidence reason:** No source content or URLs provided
- **Claim verdicts:**
```json
[
  {
    "claim": "The UK public won’t be able to claim compensation if unlicensed vaccines damage our health.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 18. AVeriTeC / av_027 - Refuted

#### Input
- **Claim:** The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** No source URLs or source text were included, so there is nothing to check against the claim that the PLAAF shot down an Indian Su-30 in Tibet. Without any provided evidence, the claim’s truth status cannot be determined from the supplied materials.
- **Confidence reason:** No sources provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 19. AVeriTeC / av_028 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** U.S. President Donald Trump has suspended all travel from China.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided to verify or refute the claim.
- **Explanation:** The prompt lists no sources (URLs or content) to check whether Trump suspended all travel from China. Without any source material, the claim cannot be evaluated against evidence.
- **Confidence reason:** No sources provided for verification.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. President Donald Trump has suspended all travel from China.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 20. AVeriTeC / av_029 - Refuted

#### Input
- **Claim:** Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to check whether Trump suspended all travel from China before the first U.S. case. Without source text, the claim about timing and whether the action was “unprecedented” cannot be evaluated.
- **Confidence reason:** No source URLs or content provided.
- **Claim verdicts:**
```json
[
  {
    "claim": "Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 21. AVeriTeC / av_030 - Supported

#### Input
- **Claim:** A Pakistani website was hacked by an Indian cyber group to wish Pawan Kalyan a Happy Birthday.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No sources were provided to verify the alleged hack or the stated motive.
- **Explanation:** No source URLs or source content were included, so there is nothing to check against the claim. Without any evidence in the provided sources, the hack attribution and birthday motive cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "A Pakistani website was hacked by an Indian cyber group to wish Pawan Kalyan a Happy Birthday.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 22. PolitiFact / pf_001 - false

#### Input
- **Claim:** Says Hillary Clinton has donated every cent shes ever earned from speaking fees to charity.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided to verify or refute the claim.
- **Explanation:** The prompt lists no sources (no URLs or content), so there is nothing to check against the claim about Hillary Clinton donating every cent from speaking fees to charity. Without source material, the claim cannot be evaluated using the provided evidence.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Hillary Clinton has donated every cent shes ever earned from speaking fees to charity.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 23. PolitiFact / pf_002 - false

#### Input
- **Claim:** Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided to verify the claim about a resolved investigation.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to check against the claim. Without any provided evidence, the claim cannot be supported or contradicted based on the supplied materials.
- **Confidence reason:** No source content provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 24. PolitiFact / pf_003 - true

#### Input
- **Claim:** Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources or URLs, so there’s nothing to verify whether Orrin Hatch co-sponsored a 1993 health care bill with an individual mandate. Without source text, I can’t determine support or contradiction.
- **Confidence reason:** No sources/URLs provided to check.
- **Claim verdicts:**
```json
[
  {
    "claim": "Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 25. PolitiFact / pf_004 - barely-true

#### Input
- **Claim:** Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** No sources were provided, so the claim can’t be checked.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there’s nothing to verify whether Mark Herring voted for shorter sentences for sex offenders. Without any source material, the claim’s accuracy cannot be assessed.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 26. PolitiFact / pf_005 - barely-true

#### Input
- **Claim:** In many instances, (peoples) health care costs are more than their mortgage costs or their rent, which, by the way, is a first in American history.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** No sources were provided, so the claims can’t be evaluated.
- **Explanation:** The prompt lists no actual sources or URLs, so there is nothing to verify whether healthcare costs exceed mortgage/rent costs or whether this is a first in American history. Without source content, the claims are not assessable.
- **Confidence reason:** No sources or URLs provided
- **Claim verdicts:**
```json
[
  {
    "claim": "In many instances, (peoples) health care costs are more than their mortgage costs or their rent, which, by the way, is a first in American history.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 27. PolitiFact / pf_006 - false

#### Input
- **Claim:** In countries where there are higher, more strict gun laws, there is more gun violence.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to check against the claim. Without any evidence, I can’t determine whether the claim is supported or contradicted by the provided materials.
- **Confidence reason:** No sources provided to assess evidence.
- **Claim verdicts:**
```json
[
  {
    "claim": "In countries where there are higher, more strict gun laws, there is more gun violence.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 28. PolitiFact / pf_007 - false

#### Input
- **Claim:** Unfortunately, since Mr. Fosters been mayor ... there are less people employed in the city of St. Petersburg than there were prior to his taking office.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided to verify whether employment in St. Petersburg fell under Mr. Foster.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to check against the claim about employment levels in St. Petersburg after Mr. Foster became mayor. Without any source material, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Unfortunately, since Mr. Fosters been mayor ... there are less people employed in the city of St. Petersburg than there were prior to his taking office.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 29. PolitiFact / pf_008 - mostly-true

#### Input
- **Claim:** "There's only four senators senior to me ... there's still 44 older than me."
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** No sources were provided, so the claim cannot be evaluated.
- **Explanation:** The prompt includes no source URLs or source text, so there is nothing to verify the statement about the number of senators older than the speaker. Without any provided evidence, the claim’s accuracy cannot be determined from the supplied materials.
- **Confidence reason:** No sources provided to check against.
- **Claim verdicts:**
```json
[
  {
    "claim": "There's only four senators senior to me ... there's still 44 older than me.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 30. PolitiFact / pf_009 - true

#### Input
- **Claim:** The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** No sources were provided to verify the Nazi-justification claim.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to check whether Nazis used the quoted slurs to justify genocide. Without source material, the claim cannot be supported or contradicted based on provided evidence.
- **Confidence reason:** No sources provided to evaluate.
- **Claim verdicts:**
```json
[
  {
    "claim": "The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 31. PolitiFact / pf_010 - mostly-true

#### Input
- **Claim:** Marijuana is less toxic than alcohol.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (the Sources section is empty), so there’s nothing to check against the claim. Without any source text or URLs, I can’t determine whether the claim is supported or contradicted.
- **Confidence reason:** No sources provided to assess evidence.
- **Claim verdicts:**
```json
[
  {
    "claim": "Marijuana is less toxic than alcohol.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 32. PolitiFact / pf_011 - true

#### Input
- **Claim:** Says Donald Trump has changed his mind on abortion.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** No sources were provided to verify whether Trump changed his mind on abortion.
- **Explanation:** The prompt lists the claim but provides no sources (no URLs or source text). Without any source material, it’s impossible to determine whether the claim is supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Donald Trump has changed his mind on abortion.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 33. PolitiFact / pf_012 - false

#### Input
- **Claim:** A new ruling by the EPA would force dairy farmers to comply with the Spill Prevention, Control and Countermeasure Program when dealing with spilt milk -- the same regulations oil and natural gas producers must follow.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the EPA dairy spill-rule claim can’t be verified.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to check whether an EPA ruling would require dairy farmers to follow SPCC rules for spilled milk or whether those rules match those for oil and natural gas producers. Without source text, the claim’s accuracy cannot be assessed.
- **Confidence reason:** No source URLs or content provided
- **Claim verdicts:**
```json
[
  {
    "claim": "A new ruling by the EPA would force dairy farmers to comply with the Spill Prevention, Control and Countermeasure Program when dealing with spilt milk -- the same regulations oil and natural gas producers must follow.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 34. PolitiFact / pf_013 - mostly-true

#### Input
- **Claim:** Missouri is #1 in the nation for holding down tuition increases at public universities.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** No sources were provided to verify Missouri’s tuition-increase ranking.
- **Explanation:** The prompt lists no sources (no URLs or content), so there is nothing to check against the claim that Missouri is #1 for holding down tuition increases at public universities. Without source material, the claim cannot be supported or contradicted.
- **Confidence reason:** No source URLs or evidence provided
- **Claim verdicts:**
```json
[
  {
    "claim": "Missouri is #1 in the nation for holding down tuition increases at public universities.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 35. PolitiFact / pf_014 - half-true

#### Input
- **Claim:** Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the 95% survey claim can’t be verified.
- **Explanation:** The prompt lists no sources or URLs, so there is nothing to check whether a survey found that 95% of people crossing the U.S.-Mexico border said they were coming because they were promised amnesty. Without the referenced survey or any supporting/contradicting material, the claim cannot be evaluated.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 36. PolitiFact / pf_015 - false

#### Input
- **Claim:** When undocumented children are picked up at the border and told to appear later in court ... 90 percent do not then show up.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the 90% non-appearance claim can’t be checked.
- **Explanation:** The prompt lists no sources or URLs, so there is no evidence to verify or refute the claim that 90% of undocumented children fail to appear in court after being told to appear later. Without source text or links, the claim cannot be evaluated using the provided materials.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "When undocumented children are picked up at the border and told to appear later in court ... 90 percent do not then show up.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 37. PolitiFact / pf_016 - half-true

#### Input
- **Claim:** John McCain "has threatened extinction for North Korea and sung songs about bombing Iran."
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim cannot be evaluated.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to verify whether John McCain threatened North Korea with extinction or sang songs about bombing Iran. Without source material, the claim’s accuracy cannot be supported or contradicted.
- **Confidence reason:** No sources provided to check the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "John McCain \"has threatened extinction for North Korea and sung songs about bombing Iran.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 38. PolitiFact / pf_017 - true

#### Input
- **Claim:** In the last 10 years, Georgias middle class income has dropped $6,500.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** No sources were provided to verify Georgia’s middle-class income change.
- **Explanation:** The prompt includes no source URLs or source content, so there’s nothing to check against the claim that Georgia’s middle-class income dropped $6,500 in the last 10 years. Without any referenced data, the claim cannot be supported or contradicted.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the last 10 years, Georgias middle class income has dropped $6,500.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 39. PolitiFact / pf_018 - half-true

#### Input
- **Claim:** Oil production is down 14 percent this year on federal land.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** No source URLs or source content were included, so there’s nothing to verify whether oil production on federal land is down 14% this year. Without any evidence, the claim’s accuracy cannot be determined from the provided materials.
- **Confidence reason:** No sources provided to assess the claim
- **Claim verdicts:**
```json
[
  {
    "claim": "Oil production is down 14 percent this year on federal land.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 40. PolitiFact / pf_019 - barely-true

#### Input
- **Claim:** Onion Creeks highest flow rate on a recent night of flooding was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** No sources were provided, so the claim can’t be checked.
- **Explanation:** The prompt lists no source URLs or source content, so there’s nothing to verify the stated 120,000 cfs peak flow for Onion Creeks or the comparison to Niagara Falls’ average flow. Without sources, the claim’s accuracy and context cannot be evaluated.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Onion Creeks highest flow rate on a recent night of flooding was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 41. PolitiFact / pf_020 - pants-fire

#### Input
- **Claim:** U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence."
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** The prompt lists no sources (URLs or text), so there’s nothing to check whether Rep. Jim Langevin said he opposed a border fence due to fear someone would be hurt. Without source material, the claim’s accuracy cannot be evaluated.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration \"because he is afraid that someone will get hurt trying to go around the fence.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 42. PolitiFact / pf_021 - half-true

#### Input
- **Claim:** Says he brought 1,200 jobs to Texas by moving his factories here from China.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided to verify the job-creation claim.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to check whether the claim about bringing 1,200 jobs to Texas by moving factories from China is supported or contradicted. Without source material, the claim cannot be evaluated using the provided evidence.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says he brought 1,200 jobs to Texas by moving his factories here from China.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 43. PolitiFact / pf_022 - mostly-true

#### Input
- **Claim:** Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** The prompt lists no source URLs or source text, so there’s nothing to check for evidence of layoffs, tax breaks, or the CEO’s donation to Kasich’s super PAC. Without the referenced sources, the claim’s accuracy cannot be evaluated.
- **Confidence reason:** No source material provided to assess.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 44. PolitiFact / pf_023 - false

#### Input
- **Claim:** Says the oil industry subsidies that President Barack Obama is attacking dont exist
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to check whether the claim about Obama attacking non-existent oil industry subsidies is supported or contradicted. Without source text, the truth of the claim cannot be determined.
- **Confidence reason:** No source material provided to verify the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says the oil industry subsidies that President Barack Obama is attacking dont exist",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 45. PolitiFact / pf_024 - half-true

#### Input
- **Claim:** Republicans are attempting to remove Barack Obama from Georgias Presidential Ballot in 2012.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** No sources were provided, so the claim cannot be evaluated.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there is nothing to verify whether Republicans attempted to remove Barack Obama from Georgia’s 2012 presidential ballot. Without any source material, the claim’s accuracy cannot be assessed.
- **Confidence reason:** No sources provided to check the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Republicans are attempting to remove Barack Obama from Georgias Presidential Ballot in 2012.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 46. PolitiFact / pf_025 - mostly-true

#### Input
- **Claim:** Federal spending on entitlements is projected to consume all revenue by 2045.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to verify whether federal entitlement spending is projected to consume all revenue by 2045. Without source text, the claim’s accuracy cannot be assessed.
- **Confidence reason:** No sources provided to check the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Federal spending on entitlements is projected to consume all revenue by 2045.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 47. PolitiFact / pf_026 - barely-true

#### Input
- **Claim:** About two-thirds of Medicaid beneficiaries are children, but they account for one-third of the programs cost, while one-third are elderly, and they account for two-thirds of the cost.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** Cannot verify the Medicaid cost-share and beneficiary-age breakdown because no sources were provided.
- **Explanation:** No sources (URLs or content) were included, so there is nothing to check the claim against. Without source data on Medicaid beneficiary age distribution and program cost shares, the claim cannot be supported or contradicted.
- **Confidence reason:** No source URLs or evidence provided.
- **Claim verdicts:**
```json
[
  {
    "claim": "About two-thirds of Medicaid beneficiaries are children, but they account for one-third of the programs cost, while one-third are elderly, and they account for two-thirds of the cost.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 48. PolitiFact / pf_027 - pants-fire

#### Input
- **Claim:** Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false`
- **TLDR:** No sources were provided, so the claim can’t be verified or refuted.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to check whether Fox News is banned in Canada or whether any law prevents news channels from lying. Without source material, the claim’s accuracy cannot be evaluated.
- **Confidence reason:** No sources provided to assess the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 49. PolitiFact / pf_028 - barely-true

#### Input
- **Claim:** Says Tom Cottons vote in Congress to change Medicare will increase out-of-pocket expenses for every senior in Arkansas.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** No sources were provided, so the claim can’t be checked.
- **Explanation:** The prompt lists no sources (no URLs or source text), so there’s nothing to verify whether Tom Cotton’s vote would increase out-of-pocket costs for every senior in Arkansas. Without any source material, the claim’s accuracy cannot be assessed.
- **Confidence reason:** No sources provided to evaluate the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Tom Cottons vote in Congress to change Medicare will increase out-of-pocket expenses for every senior in Arkansas.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 50. PolitiFact / pf_029 - mostly-true

#### Input
- **Claim:** Says Hillary Clinton called the Trans-Pacific Partnership the gold standard. You called it the gold standard of trade deals. You said its the finest deal youve ever seen.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** No sources were provided, so the claims can’t be verified or refuted.
- **Explanation:** The prompt lists no source URLs or source text, so there is nothing to check whether Hillary Clinton or the speaker made the quoted statements about the Trans-Pacific Partnership. Without any provided sources, the evidence for or against the claims is unavailable.
- **Confidence reason:** No sources provided to evaluate the claims.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Hillary Clinton called the Trans-Pacific Partnership the gold standard. You called it the gold standard of trade deals. You said its the finest deal youve ever seen.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 51. PolitiFact / pf_030 - true

#### Input
- **Claim:** Today California is kicking our butt, creating more jobs and more economic growth than Texas.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** No sources were provided, so the claim can’t be evaluated.
- **Explanation:** The prompt lists no sources (URLs or content), so there’s nothing to check against the claim about California vs. Texas jobs and economic growth. Without source material, the truth of the statement cannot be determined.
- **Confidence reason:** No sources provided to verify or refute.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today California is kicking our butt, creating more jobs and more economic growth than Texas.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Evidence Input
_No evidence sources captured or found in cache._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

## Arm A - Gold Evidence

Failures shown: 12

### 1. AVeriTeC / av_001 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Indian Railways has been completely privatized, and as a result, scores of people working in the Railways would lose their jobs.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `10`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** score got `10`, expected `25-75`
- **TLDR:** Sources say there will be no job losses and privatization is not complete.
- **Explanation:** Source 1 indicates privatization is not complete: it says public-private partnership may be worked upon but control will still vest with @RailMinIndia, and explicitly states “No jobs are being lost.” Source 2 similarly says “No job cuts, but profiles may change,” contradicting the claim that complete privatization would cause many job losses.
- **Confidence reason:** Both sources directly deny job losses and full privatization.
- **Claim verdicts:**
```json
[
  {
    "claim": "Indian Railways has been completely privatized, and as a result, scores of people working in the Railways would lose their jobs.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20200909075240im_/https://pbs.twimg.com/profile_banners/1207634475254865921/1598874762/1500x500": "contradicting",
  "https://web.archive.org/web/20211206134459/https://www.livemint.com/news/india/no-job-cuts-but-profiles-may-change-says-indian-railways-11593790324156.html": "contradicting"
}
```

#### Gold Evidence Input
1. **Has the government-owned Indian Railways been fully privatised?**
   URL: https://web.archive.org/web/20200909075240im_/https://pbs.twimg.com/profile_banners/1207634475254865921/1598874762/1500x500
   Content: There are certain areas where public-private partnership is being worked upon but the control will still vest with @RailMinIndia. No jobs are being lost.

2. **Will there be Job losses due to the partial privatization?**
   URL: https://web.archive.org/web/20211206134459/https://www.livemint.com/news/india/no-job-cuts-but-profiles-may-change-says-indian-railways-11593790324156.html
   Content: No job cuts, but profiles may change says Indian Railways.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_002 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Donald Trump said: "Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children."
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** The sources don’t show Trump’s quoted claim about Biden opposing school choice or closing charters.
- **Explanation:** Source 3 says Biden supports “good charter schools” and allowing students to pick among public schools, which is inconsistent with the claim that Biden vowed to oppose school choice and close down charter schools. However, none of the sources provide evidence that Trump actually said the specific quoted wording, and Source 4 only mentions the Biden administration pushing for more oversight, not closing charter schools. Source 1 and Source 2 define school choice and charter schools but do not address Biden’s or Trump’s statements.
- **Confidence reason:** No source verifies Trump’s exact quote; Biden stance only partially covered.
- **Claim verdicts:**
```json
[
  {
    "claim": "Donald Trump said: \"Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.edchoice.org/school-choice/what-is-school-choice/#:~:text=In%20a%20nutshell%3A%20School%20choice,other%20learning%20environment%20families%20choose.": "neutral",
  "https://en.wikipedia.org/wiki/Charter_schools_in_the_United_States#:~:text=Charter%20schools%20in%20the%20United%20States%20are%20primary%20or%20secondary,funded%20with%20public%20tax%20dollars.": "neutral",
  "https://web.archive.org/web/20210118102704/https://www.edchoice.org/school-choice/types-of-school-choice/": "contradicting",
  "https://www.edweek.org/policy-politics/federal-funding-and-charter-school-closures-what-the-latest-government-data-show/2022/10": "neutral"
}
```

#### Gold Evidence Input
1. **What is 'school choice'**
   URL: https://www.edchoice.org/school-choice/what-is-school-choice/#:~:text=In%20a%20nutshell%3A%20School%20choice,other%20learning%20environment%20families%20choose.
   Content: School choice allows public education funds to follow students to the schools or services that best fit their needs —whether that’s to a public school, private school, charter school, home school or any other learning environment families choose

2. **What are U.S charter schools?**
   URL: https://en.wikipedia.org/wiki/Charter_schools_in_the_United_States#:~:text=Charter%20schools%20in%20the%20United%20States%20are%20primary%20or%20secondary,funded%20with%20public%20tax%20dollars.
   Content: Charter schools in the United States are primary or secondary education institutions that are funded through taxation and operated by private organizations, rather than local school districts. They do not charge tuition, as they are funded with public tax dollars

3. **Did Joe Biden oppose school choice?**
   URL: https://web.archive.org/web/20210118102704/https://www.edchoice.org/school-choice/types-of-school-choice/
   Content: he supports good charter schools and allowing students to pick among public schools. Those also qualify as school choice options.

4. **Did Joe Biden want to close down charter schools?**
   URL: https://www.edweek.org/policy-politics/federal-funding-and-charter-school-closures-what-the-latest-government-data-show/2022/10
   Content: The Biden administration did controversially push for more oversight when it comes to charter school funding.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_005 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Russia sent medical aid to the US, in the form of medical equipment to help coronavirus patients.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** score got `78`, expected `25-75`
- **TLDR:** Russia sent ventilators to the US, but the US government described it as a purchase.
- **Explanation:** Source 1 says a Russian military plane delivered 60 tons of medical equipment to JFK, including 45 Aventa-M ventilators intended to help coronavirus patients. However, Source 2 states the U.S. State Department clarified the shipment as a “purchase” rather than aid, indicating the “aid” framing is disputed.
- **Confidence reason:** Two sources directly address shipment; aid-vs-purchase is contested.
- **Claim verdicts:**
```json
[
  {
    "claim": "Russia sent medical aid to the US, in the form of medical equipment to help coronavirus patients.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210718091632/https://www.nytimes.com/2020/04/02/world/europe/coronavirus-us-russia-aid.html": "supporting",
  "https://web.archive.org/web/20210718091632/https://www.state.gov/u-s-purchase-of-needed-supplies-from-russia/": "contradicting",
  "https://web.archive.org/web/20210718091632/https://www.buzzfeednews.com/article/christopherm51/fema-russia-ventilators-coronavirus?fbclid=IwAR0NDhdqILPthpTHGNnmK_-8yH7CjmyDtbo81pzlHEVVKI9loXMnfI9uVas": "neutral"
}
```

#### Gold Evidence Input
1. **What did Russia send to the US during the covid-19 outbreak?**
   URL: https://web.archive.org/web/20210718091632/https://www.nytimes.com/2020/04/02/world/europe/coronavirus-us-russia-aid.html
   Content: On April 1, a Russian military plane arrived at New York’s JFK Airport loaded with 60 tons of medical equipment, including 45 Russian-produced Aventa-M ventilators meant to help coronavirus patients in intensive care keep breathing.

2. **Was this aid, or was this a purchase from the US?**
   URL: https://web.archive.org/web/20210718091632/https://www.state.gov/u-s-purchase-of-needed-supplies-from-russia/
   Content: Initially, there was confusion over whether the planeload of equipment was aid, as Russia portrayed it, or if the American side had paid for it. The U.S. State Department clarified this in a press release that referred to the shipment as a “purchase.”

3. **What happened to this equipment?**
   URL: https://web.archive.org/web/20210718091632/https://www.buzzfeednews.com/article/christopherm51/fema-russia-ventilators-coronavirus?fbclid=IwAR0NDhdqILPthpTHGNnmK_-8yH7CjmyDtbo81pzlHEVVKI9loXMnfI9uVas
   Content: Within about one week, Aventa-M ventilators had been found responsible for fires at two Russian hospitals in Moscow and St. Petersburg; six people were killed. Russian investigators blamed the ventilators’ faulty circuitry. Ultimately the Aventa-M ventilators from Russia were never used by any American hospital, but in October it was finally discovered where those ventilators ended up – in the trash heap. This week, Christopher Miller, writing for Buzzfeed, revealed that the Federal Emergency Management Agency (FEMA) disposed of the Aventa-M ventilators.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false, mostly_false`; score got `78`, expected `0-40`
- **TLDR:** Employment rose from 132,310 (2002/03) to 192,277 (2018/19), about a 45% increase—close to 50%.
- **Explanation:** Source 1 reports 132,310 people employed in the SA police force in 2002/03, while Source 2 reports 192,277 employed in 2018/19. That change is an increase of roughly 45% (consistent with Source 3’s 45.3% figure), which is close to but not exactly 50%. Therefore, the “since 2002” growth is supported directionally but not precisely by the provided sources.
- **Confidence reason:** Only one computed percentage source; dates differ slightly (2002/03 vs 2018/19).
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20200918235056/https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/documents/2003/saps_annreport_0203_part3.pdf#page=5": "supporting",
  "https://web.archive.org/web/20210603081707/https://www.saps.gov.za/about/stratframework/annual_report/2018_2019/saps_annualreport2018_2019v2.pdf#page=41": "supporting",
  "https://www.calculator.net/": "supporting"
}
```

#### Gold Evidence Input
1. **How many people were employed in the SA police force in 2002/03**
   URL: https://web.archive.org/web/20200918235056/https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/documents/2003/saps_annreport_0203_part3.pdf#page=5
   Content: 132,310

2. **How many people were employed in SA police force in 2018/19**
   URL: https://web.archive.org/web/20210603081707/https://www.saps.gov.za/about/stratframework/annual_report/2018_2019/saps_annualreport2018_2019v2.pdf#page=41
   Content: 192,277

3. **What is the percentage growth in the SA police force between 2002 to 2019**
   URL: https://www.calculator.net/
   Content: 45.3%

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_012 - Not Enough Evidence

#### Input
- **Claim:** Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `false`
- **Score:** `10`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `unverifiable, mixed`; score got `10`, expected `30-60`
- **TLDR:** The sources do not substantiate the alleged child torture/rape images on Hunter Biden’s laptop.
- **Explanation:** Source 1 only says Hunter Biden’s laptop was subpoenaed and that an FBI agent worked on child pornography; it provides no evidence of 25,000 photos or of torture/rape of children under 10 in China. Source 2 discusses a whistleblower claim about a laptop and that the FBI would not confirm or deny details, but it does not provide confirmation of the specific allegations in the claim.
- **Confidence reason:** Both sources omit the specific alleged content and quantities.
- **Claim verdicts:**
```json
[
  {
    "claim": "Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://twitter.com/atrupar/status/1317849887438966784?s=21": "neutral",
  "https://www.foxnews.com/politics/sen-johnson-presses-wray-on-validity-of-hunter-biden-laptop-claim": "neutral"
}
```

#### Gold Evidence Input
1. **What is this claim based on?**
   URL: https://twitter.com/atrupar/status/1317849887438966784?s=21
   Content: Hunter Biden's laptop was subpoena'd by an FBI agent who workd on child pornography.

2. **Was there child pornography on the laptop?**
   URL: https://www.foxnews.com/politics/sen-johnson-presses-wray-on-validity-of-hunter-biden-laptop-claim
   Content: Sen. Ron Johnson is calling on FBI Director Christopher Wray to confirm or deny details regarding a laptop said to have belonged to Democratic presidential nominee Joe Biden's son Hunter Biden. Johnson, R-Wis., said in a letter to Wray obtained by Fox News that a whistleblower contacted his committee on September 24, claiming to possess a laptop that Hunter Biden left at his business, and that he had turned it over to the FBI. Johnson noted that staff immediately asked the FBI to confirm certain details in order to validate the claim, but the bureau said they would not confirm or deny any of the information included in their request.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_013 - Refuted

#### Input
- **Claim:** Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`; score got `50`, expected `0-40`
- **TLDR:** Sources don’t verify the 21-times claim or its medical basis.
- **Explanation:** Source 1 states an article’s claim that Ebeneezer is a medical doctor and herbal practitioner at Amuzu Hospital, but it does not provide enough detail in the excerpt to confirm the instruction about having sex 21 times per month. Source 2 only addresses whether sex/ejaculation amount is linked to prostate cancer, without confirming any specific recommendation of “21 times a month.”
- **Confidence reason:** Insufficient source detail on the exact 21-times instruction.
- **Claim verdicts:**
```json
[
  {
    "claim": "Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210119165100/https://www.westafricareporters.com/men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer-expert/": "neutral",
  "https://web.archive.org/web/20201228105910/https://www.sciencedirect.com/science/article/abs/pii/S0302283816003778?via%3Dihub": "neutral"
}
```

#### Gold Evidence Input
1. **Who is Dr Ebeneezer?**
   URL: https://web.archive.org/web/20210119165100/https://www.westafricareporters.com/men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer-expert/
   Content: The original article claims Ebeneezer is a medical doctor and a herbal practitioner at the Amuzu Hospital

2. **Is amount of sex or ejaculation linked to prostate cancer?**
   URL: https://web.archive.org/web/20201228105910/https://www.sciencedirect.com/science/article/abs/pii/S0302283816003778?via%3Dihub
   Content: Yes

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_015 - Not Enough Evidence

#### Input
- **Claim:** In the US lockdowns are partly responsible for excess deaths not directly attributed to COVID-19 which were observed in 2020.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources don’t support lockdowns causing excess deaths; they explicitly omit lockdown factors.
- **Explanation:** Source 1 (CDC MMWR) estimates excess deaths in 2020 and notes that excess deaths may include deaths directly or indirectly associated with COVID-19, but it does not attribute the non-COVID portion to lockdowns. Sources 2 and 3 state that the studies used do not mention lockdown factors in the excessive deaths, contradicting the claim that lockdowns are partly responsible.
- **Confidence reason:** Sources explicitly omit lockdown attribution.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the US lockdowns are partly responsible for excess deaths not directly attributed to COVID-19 which were observed in 2020.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm": "neutral",
  "https://web.archive.org/web/20210310112506/https://jamanetwork.com/journals/jama/fullarticle/2771761": "contradicting",
  "https://web.archive.org/web/20210309181157/https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm": "contradicting"
}
```

#### Gold Evidence Input
1. **How is  lockdown partly responsible for excess deaths in the US ?**
   URL: https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm
   Content: As of October 15, 216,025 deaths from coronavirus disease 2019 (COVID-19) have been reported in the United States*; however, this number might underestimate the total impact of the pandemic on mortality. Measures of excess deaths have been used to estimate the impact of public health pandemics or disasters, particularly when there are questions about underascertainment of deaths directly attributable to a given event or cause (1–6).† Excess deaths are defined as the number of persons who have died from all causes, in excess of the expected number of deaths for a given place and time. This report describes trends and demographic patterns in excess deaths during January 26–October 3, [...]

2. **Do the studies used to make the claim include lockdowns relating to excessive deaths?**
   URL: https://web.archive.org/web/20210310112506/https://jamanetwork.com/journals/jama/fullarticle/2771761
   Content: they do not mention lockdown factors in the excessive deaths

3. **Do the studies used to make the claim include lockdowns relating to excessive deaths?**
   URL: https://web.archive.org/web/20210309181157/https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm
   Content: they do not mention lockdown factors in the excessive deaths

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_018 - Not Enough Evidence

#### Input
- **Claim:** There was a 40% drop in the price of oil, Nigeria's main export.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources don’t support a 40% oil-price drop; one cites a 73% fall from Jan–Apr 2020.
- **Explanation:** Source 1 reports that Nigeria’s monthly average oil prices decreased 73% from January to April 2020, not 40%. Source 2 only discusses that oil prices fluctuate, without giving any specific percentage drop or linking it to a 40% decline.
- **Confidence reason:** Only one source provides a specific drop figure; it differs.
- **Claim verdicts:**
```json
[
  {
    "claim": "There was a 40% drop in the price of oil, Nigeria's main export.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210405033525/https://nnpcgroup.com/NNPCDocuments/Performance%20Data/FullReports/NNPC%20Monthly%20Financial%20and%20Operations%20Report%20for%20the%20Month%20of%20July%202020.pdf": "supporting",
  "https://scialert.net/fulltext/?doi=aujss.2017.1.16#:~:text=The%20surplus%20of%20exporting%20value,great%20challenges%20for%20policy%20making.": "neutral"
}
```

#### Gold Evidence Input
1. **How much did Nigerian oil prices fall in 2020?**
   URL: https://web.archive.org/web/20210405033525/https://nnpcgroup.com/NNPCDocuments/Performance%20Data/FullReports/NNPC%20Monthly%20Financial%20and%20Operations%20Report%20for%20the%20Month%20of%20July%202020.pdf
   Content: According to data from July 2020 from the Nigerian National Petroleum Corporation, monthly average prices decreased 73% from January to April 2020.

2. **Are there frequent fluctuations in Nigeria's oil prices?**
   URL: https://scialert.net/fulltext/?doi=aujss.2017.1.16#:~:text=The%20surplus%20of%20exporting%20value,great%20challenges%20for%20policy%20making.
   Content: Oil prices have witnessed profound fluctuations and this has implications for the performance of macroeconomic variables, posing great challenges for policy making.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_019 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** The sources don’t show Twitter warned about Biden fracking clips specifically.
- **Explanation:** Source 1 discusses general election-related changes, including prompting users to add commentary via Quote Tweet and a warning about not having opened and read content before retweeting. Source 2 only states “Yes” to a question about warnings on unedited Biden fracking tweets, but it provides no supporting details or evidence. Because the sources don’t directly connect the described warning behavior to Biden fracking clips, the claim can’t be confirmed or refuted from the provided material.
- **Confidence reason:** Only one source asserts “Yes” without evidence; others are general.
- **Claim verdicts:**
```json
[
  {
    "claim": "Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20201101032342/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html": "neutral",
  "https://web.archive.org/web/20201101024709/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html": "neutral"
}
```

#### Gold Evidence Input
1. **Have Twitter started putting warnings on tweets that are just unedited clips of Biden saying he would end fracking?**
   URL: https://web.archive.org/web/20201101032342/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html
   Content: Twitter automatically warns when the user has not opened and read the item to be re-tweeted. "Headlines don't tell the whole story," the Twitter message says. "You can read the article on Twitter before Retweeting." Twitter announced a set of changes to try to stem the spread of misinformation ahead of the November 3, 2020 presidential election. Among the most significant is a request that users add their own content before retweeting someone else's: (W)e will encourage people to add their own commentary prior to amplifying content by prompting them to Quote Tweet instead of Retweet. People who go to Retweet will be brought to the Quote Tweet composer where they'll be encouraged to [...]

2. **Had Twitter been putting warnings on un-edited tweets about Biden saying he would end fracking at the time of the claim (October 2020)?**
   URL: https://web.archive.org/web/20201101024709/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html
   Content: Yes

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_023 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Even if your mail-in ballot is postmarked prior to the Election day but arrives after the Election day it will be thrown out.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources don’t show a universal rule about postmarked-before-but-arriving-after ballots being discarded.
- **Explanation:** Source 2 only states that Wisconsin (and about 30 states) require absentee ballots to be received by Election Day to be counted, which does not specifically address the scenario where a ballot is postmarked before but arrives after. Source 1 and Source 3 do not provide information about what happens to late-arriving, pre-postmarked ballots.
- **Confidence reason:** Only indirect coverage; no source addresses the exact scenario.
- **Claim verdicts:**
```json
[
  {
    "claim": "Even if your mail-in ballot is postmarked prior to the Election day but arrives after the Election day it will be thrown out.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.buzzfeednews.com/article/addybaird/vote-by-mail-state-deadlines": "neutral",
  "https://www.cbsnews.com/news/wisconsin-election-supreme-court-rules-againt-absentee-ballots-after-election-day/": "neutral",
  "https://www.facebook.com/GilbertLiz/photos/a.356148997800555/3549940058421417": "neutral"
}
```

#### Gold Evidence Input
1. **Do some states accept ballots that were postmarked before election day?**
   URL: https://www.buzzfeednews.com/article/addybaird/vote-by-mail-state-deadlines
   Content: There are 22 states plus the District of Columbia

2. **Are there states which do require votes to arrive by election day.**
   URL: https://www.cbsnews.com/news/wisconsin-election-supreme-court-rules-againt-absentee-ballots-after-election-day/
   Content: Wisconsin is one of about 30 states that require absentee ballots be received by Election Day to be counted.

3. **Does the original posterLiz Gilbert mention the state that does not allow voting after deadline?**
   URL: https://www.facebook.com/GilbertLiz/photos/a.356148997800555/3549940058421417
   Content: No

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. AVeriTeC / av_029 - Refuted

#### Input
- **Claim:** Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`; score got `50`, expected `0-40`
- **TLDR:** The sources don’t confirm Trump suspended all China travel before the first U.S. case.
- **Explanation:** Source 1 only provides the date the first U.S. COVID-19 travel-related case was discovered (21 January 2020) and does not mention any presidential action or a China travel suspension. Source 2 discusses travel restrictions and their impact after Trump’s restrictions, but it does not establish that the action was “before the first case” or that it suspended “all travel from China.”
- **Confidence reason:** Sources omit key timing and scope details.
- **Claim verdicts:**
```json
[
  {
    "claim": "Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210502100658/https://www.cdc.gov/media/releases/2020/p0121-novel-coronavirus-travel-case.html": "neutral",
  "https://web.archive.org/web/20210503140609/https://www.nytimes.com/2020/04/04/us/coronavirus-china-travel-restrictions.html": "neutral"
}
```

#### Gold Evidence Input
1. **When was the first case of COVID-19 discovered in the US**
   URL: https://web.archive.org/web/20210502100658/https://www.cdc.gov/media/releases/2020/p0121-novel-coronavirus-travel-case.html
   Content: 21st January 2020

2. **How many people were still travelling after the travel ban on China after the discovery of the novel coronavirus in the US**
   URL: https://web.archive.org/web/20210503140609/https://www.nytimes.com/2020/04/04/us/coronavirus-china-travel-restrictions.html
   Content: There were 1,300 direct flights to 17 cities before President Trump’s travel restrictions. Since then, nearly 40,000 Americans and other authorized travelers have made the trip

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. AVeriTeC / av_030 - Supported

#### Input
- **Claim:** A Pakistani website was hacked by an Indian cyber group to wish Pawan Kalyan a Happy Birthday.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `true, mostly_true`; score got `55`, expected `60-100`
- **TLDR:** Sources support Pakistani hacks by Indian cyber groups, but not the birthday motive conclusively.
- **Explanation:** Sources 4 and 5 state that Pakistani websites were hacked by Indian hackers/cyber groups. Source 6 says birthday messages for Pawan Kalyan appeared on hacked Pakistani websites, but the provided sources do not explicitly connect this to “an Indian cyber group” performing the hack specifically to wish him a Happy Birthday. Source 3 is general background about hacking, and Source 2 provides no accessible content.
- **Confidence reason:** Hacking is supported; birthday intent linkage is not fully explicit.
- **Claim verdicts:**
```json
[
  {
    "claim": "A Pakistani website was hacked by an Indian cyber group to wish Pawan Kalyan a Happy Birthday.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "Metadata": "neutral",
  "https://www.facebook.com/IndianCyberTroops/posts/635643360421831": "neutral",
  "https://insidergeeks.com/indian-cyber-troops-again-hacked-nepali-website/": "neutral",
  "https://web.archive.org/web/20201001082923/https://newsd.in/pakistan-website-hacked-indian-hackers-write-ramlalla-hum-aaege-mandir-karachi-lahore-me-banaege/": "supporting",
  "https://web.archive.org/web/20210603203816/https://zeenews.india.com/india/indian-hackers-give-befitting-reply-to-pakistans-agenda-on-ram-temple-kashmir-hack-over-80-pakistani-websites-2303465.html": "supporting",
  "https://web.archive.org/web/20221212111529/https://www.youtube.com/watch?v=lm-sPzoP_Jw": "supporting"
}
```

#### Gold Evidence Input
1. **Where was this claim published?**
   URL: Metadata
   Content: Indian Cyber Troops

2. **Where was this claim published?**
   URL: https://www.facebook.com/IndianCyberTroops/posts/635643360421831
   Content: Content is no longer available on Facebook

3. **Who are Indian Cyber Troops?**
   URL: https://insidergeeks.com/indian-cyber-troops-again-hacked-nepali-website/
   Content: It’s not a new thing these days to hear Indian Cyber Troops hacking Nepali websites. Gradually time and again the action is repeated

4. **Were Pakistani websites hacked by Indian cyber troops?**
   URL: https://web.archive.org/web/20201001082923/https://newsd.in/pakistan-website-hacked-indian-hackers-write-ramlalla-hum-aaege-mandir-karachi-lahore-me-banaege/
   Content: Yes

5. **Were Pakistani websites hacked by Indian cyber troops?**
   URL: https://web.archive.org/web/20210603203816/https://zeenews.india.com/india/indian-hackers-give-befitting-reply-to-pakistans-agenda-on-ram-temple-kashmir-hack-over-80-pakistani-websites-2303465.html
   Content: Yes

6. **Did Indian cyber troops wish Pawan Kalyan a Happy Birthday when they hacked Pakistani websites?**
   URL: https://web.archive.org/web/20221212111529/https://www.youtube.com/watch?v=lm-sPzoP_Jw
   Content: Birthday messages for Pawan Kalyan did appear on the hacked Pakistani websites.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

## Arm B - Searched Evidence

Failures shown: 24

### 1. AVeriTeC / av_006 - Not Enough Evidence

#### Input
- **Claim:** Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `15`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say the 2020 ranking was not released and the “third most terrorised” claim used 2019 data.
- **Explanation:** HumAngle and AFP report that the viral claim about Nigeria being third in the 2020 Global Terrorism Index was misleading because the 2020 ranking had not been released and the figures shown were from 2019. FactCheckHub similarly says the infographic was misleading and that the order reflected older data rather than the released 2020 ranking.
- **Confidence reason:** Multiple fact-checks directly address and refute the 2020 ranking claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/": "contradicting",
  "https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/": "contradicting",
  "https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa": "contradicting",
  "https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism": "neutral",
  "https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf": "neutral"
}
```

#### Search Evidence Input
1. **Factcheck: Nigeria Not Ranked Third Most Terrorised Country In 2020 - HumAngle**
   URL: https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/
   Content: A Twitter account belonging to the leader of the Indigenous People of Biafra, Nnamdi Kanu, claimed on September 9 that Nigeria ranked second in the world, but this is not true. (The tweet was retweeted over 5,000 times and liked by over 4,200 users.) The report ranked Nigeria as the third-worst among a total of 163 countries, behind Afghanistan and Iraq. Trailing after the country were Syria, Pakistan, Somalia, India, Yemen, Philippines, and D.R. Congoㅡ as reported by TVC. Kanu quoted the GTI as stating that “the countries most heavily affected by terrorism are Iraq, Afghanistan, #Nigeria, Pakistan and Syria. Terrorism increased most significantly in Nigeria, where deaths increased by [...]

2. **Misleading 2020 global terrorism ranking resurfaces online - FactCheckHub**
   URL: https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/
   Content: However, when the 2020 list was released, Nigeria still ranked third and Afghanistan and Iraq ranked first and second respectively as shared in the image. Even though the countries on the list remained the same, the ranking for five of them had changed. The infographic has Afghanistan, Iraq, Nigeria, Syria, Pakistan, Somalia, India, Yemen, Philippines and DR Congo as the top ten, the actual ranking released differs in order; Afghanistan, Iraq, Nigeria, Syria, Somalia, Yemen, Pakistan, India, Democratic Republic of the Congo and Philippines. [...] # THE FINDINGS In 2020, The FactCheckHub verified the graphic which originated from TVC and found it to be misleading. The station on one of [...]

3. **Old data circulates claiming Nigeria is the most terrorised country in Africa | Fact Check**
   URL: https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa
   Content: Image A screenshot taken September 23, 2020, showing the TVC programme Nigerian channel TVC News first ran the story on September 10, 2020. It also shared its report on YouTube, with the caption “Nigeria Emerges Most Terrorised Country In Africa, Ranks Worse Than Syria, Yemen, Somalia”. The report has since popped up in Facebook and Twitter posts, and in various blogs and articles. The Daily Times newspaper shared a screenshot from TVC News's report on Facebook on September 13, 2020, with the caption “Nigeria now above Syria, Somalia, Yemen in terrorism index as the country climbs to third position”. Chidi Odinkalu, a professor and former chairman of the country’s National Human Rights [...]

4. **Global Terrorism Index 2020: Measuring the impact of terrorism - World | ReliefWeb**
   URL: https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism
   Content: ISIL’s shift to sub-Saharan Africa meant that the region recorded the second highest number of terrorism deaths, even after accounting for the substantial fall in Nigeria. Deaths attributed to ISIL affiliates in the region were recorded as far south as Mozambique and 41 per cent of all ISIL-related attacks in 2019 occurred in sub-Saharan Africa. [...] In 2019, deaths from terrorism fell for the fifth consecutive year, after peaking in 2014. The total number of deaths fell by 15.5 per cent to 13,826. The fall in deaths was mirrored by a reduction in the impact of terrorism, with 103 countries recording an improvement on their GTI score, compared to 35 that recorded a deterioration. The [...]

5. **[PDF] 2024 Global Terrorism Index - Institute for Economics & Peace**
   URL: https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf
   Content: Section 1 | RESULTS ­ 6 ­ | GLOBAL TERRORISM INDEX 2024 1 Burkina Faso 8.571 long-arrow-alt-up 1 2 Israel 8.143 long-arrow-alt-up 24 3 Mali 7.998 long-arrow-alt-up 1 4 Pakistan 7.916 long-arrow-alt-up 3 5 Syria 7.890 Arrows-alt-h 6 Afghanistan 7.825 LONG-ARROW-ALT-DOWN 5 7 Somalia 7.814 LONG-ARROW-ALT-DOWN 4 8 Nigeria 7.575 Arrows-alt-h 9 Myanmar 7.536 Arrows-alt-h 10 Niger 7.274 Arrows-alt-h 11 Iraq 7.078 LONG-ARROW-ALT-DOWN 5 12 Cameroon 6.98 LONG-ARROW-ALT-DOWN 1 13 Democratic Republic of the Congo 6.514 long-arrow-alt-up 1 14 India 6.324 LONG-ARROW-ALT-DOWN 1 15 Mozambique 6.267 LONG-ARROW-ALT-DOWN 3 16 Colombia 6.188 LONG-ARROW-ALT-DOWN 1 17 Chile 5.679 LONG-ARROW-ALT-DOWN 1 18 [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_007 - Not Enough Evidence

#### Input
- **Claim:** Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources mostly say increased enforcement and barriers can increase smuggling, not decrease it.
- **Explanation:** Source 1 explicitly argues that expanded border enforcement increases human smuggling and that enforcement can fuel reliance on smugglers. Source 4 similarly describes a mechanism where increased enforcement can lead to more use of professional smugglers (and links smuggling dynamics to border crime), which contradicts the claim that barriers reduce illegal drug and smuggling activity. While Sources 3 and 2 discuss declines in illegal entries and barrier effectiveness, they do not provide evidence that illegal drug smuggling and human smuggling decreased specifically in areas where barriers were deployed.
- **Confidence reason:** Direct contradiction from Source 1; other sources don’t address barriers’ effect on drugs/smuggling.
- **Claim verdicts:**
```json
[
  {
    "claim": "Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf": "contradicting",
  "https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers": "supporting",
  "https://cmsny.org/publications/jmhs-is-border-enforcement-effective/": "supporting",
  "https://ccis.ucsd.edu/_files/wp131.pdf": "contradicting",
  "https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025": "neutral"
}
```

#### Search Evidence Input
1. **[PDF] nfap policy brief » may 2022 - human smuggling and us immigration ...**
   URL: https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf
   Content: Spener described how three Mexican men managed to smuggle 600 people into the United States in a year working part-time. He interviewed a U.S. federal judge who “had seen hundreds, if not thousands, of ‘alien smuggling’ defendants in his courtroom over the years.” When the judge asked defendants why they decided to smuggle people into the U.S. one of the most common answers he received was “Se me hizo fácil [it just seemed easy to me].”5 Given the low barriers to entry, it should be clear that it is impossible to end human smuggling through policies based solely or primarily on immigration enforcement. EXPANDED BORDER ENFORCEMENT HAS INCREASED HUMAN SMUGGLING Expanding immigration [...]

2. **The Border Wall System is Deployed, Effective, and Disrupting Criminals and Smugglers | Homeland Security**
   URL: https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers
   Content: [...]

3. **Is Border Enforcement Effective? What We Know and What it Means - The Center for Migration Studies of New York (CMS)**
   URL: https://cmsny.org/publications/jmhs-is-border-enforcement-effective/
   Content: The new evidence suggests that unauthorized migration across the southern border has plummeted, with successful illegal entries falling from roughly 1.8 million in 2000 to just 200,000 by 2015. Border enforcement has been a significant reason for the decline — in particular, the growing use of “consequences” such as jail time for illegal border crossers has had a powerful effect in deterring repeated border crossing efforts. The success of deterrence through enforcement has meant that attempted crossings have fallen dramatically even as the likelihood of a border crosser being apprehended by the Border Patrol has only risen slightly, to just over a 50-50 chance. [...] These research [...]

4. **[PDF] The Effect of Illegal Immigration and Border Enforcement on Crime ...**
   URL: https://ccis.ucsd.edu/_files/wp131.pdf
   Content: led to an increased use of professional smugglers which in turn has led to more violence on the border. JEL classification: J61, K42 Key words: crime, immigration policy, illegal immigration, human smuggling 2 The 1990s saw a remarkable decline in crime rates not only in the U.S. as a whole, but also along the U.S.-Mexico border. Between 1991 and 2000, the median border county crime rate fell 34 percent while the U.S. crime rate fell 30 percent. It is tempting to attribute the steeper decline in border crime to stepped-up border enforcement since over the same period, although the number of illegal immigrant apprehensions rose 121 percent, border patrol enforcement (as measured by [...]

5. **Border Crossings Once Again at a Record Low in November 2025 | Homeland Security**
   URL: https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025
   Content: [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The sources don’t provide police-force growth data since 2002.
- **Explanation:** None of the provided sources include figures showing how many South Africa’s police force members there were in 2002 versus later years, nor do they state a 50% growth figure. Source 2 discusses police shortages and international comparisons, but it does not give the specific “since 2002 grew by 50%” statistic.
- **Confidence reason:** No source contains the needed 2002-to-present growth numbers.
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf": "neutral",
  "https://groundup.org.za/article/south-africas-police-shortage/": "neutral",
  "https://en.wikipedia.org/wiki/South_African_Police_Service": "neutral",
  "https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf": "neutral",
  "https://en.wikipedia.org/wiki/Crime_in_South_Africa": "neutral"
}
```

#### Search Evidence Input
1. **[PDF] south-african-police-service-annual-report-2024-2025.pdf**
   URL: https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf
   Content: ▪ Implementation of the Rome Statute of the International Criminal Court Act, 2002 (Act No 27 of 2002) ▪ International Co-operation in Criminal Matters Act, 1996 (Act No 75 of 1996) ▪ Liquor Act, 2003 (Act No 59 of 2003) and the various Provincial Liquor Acts 24 SOUTH AFRICAN POLICE SERVICE | ANNUAL REPORT 2024/2025 ▪ Marine Living Resources Act, 1998 (Act No 8 of 1998) ▪ Mental Healthcare Act, 2002 (Act No 17 of 2002) ▪ National Conventional Arms Control Act, 2002 (Act No 41 of 2002) ▪ National Environmental Management Act, 1998 (Act No 107 of 1998) ▪ National Road Traffic Act, 1996 (Act No 93 of 1996) ▪ National Strategic Intelligence Act, 1994 (Act No 39 of 1994) ▪ Non-proliferation [...]

2. **How the size of South Africa’s police force compares to other countries | GroundUp**
   URL: https://groundup.org.za/article/south-africas-police-shortage/
   Content: GroundUp Logo # How the size of South Africa’s police force compares to other countries ## The country has a growing shortage of detectives | By GroundUp and The Outlier Charts | South Africa Despite a much higher violent crime rate, South Africa has fewer police per 100,000 people than the US, UK, France, Italy and China. But we do have a higher police per person ratio than developing countries like Kenya, India and Nigeria. We also have more police per population than Canada and Japan, though they have extremely low violent crime rates. ## Growing shortage of detectives [...] Charts produced by The Outlier in partnership with GroundUp ### More about Policing Durban rape cover-up [...]

3. **South African Police Service - Wikipedia**
   URL: https://en.wikipedia.org/wiki/South_African_Police_Service
   Content: | v t e South Africa articles | [...] | v t e Law enforcement in South Africa | [...] | v t e Law enforcement in Africa |

4. **[PDF] South African Police Service Annual Report 2023/2024**
   URL: https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf
   Content: (Act No 58 of 1959) » Implementation of the Rome Statute of the International Criminal Court Act, 2002 (Act No 27 of 2002) » International Co-operation in Criminal Matters Act, 1996 (Act No 75 of 1996) » Liquor Act, 2003 (Act No 59 of 2003) and the various Provincial Liquor Acts » Marine Living Resources Act, 1998 (Act No 8 of 1998) » Mental Healthcare Act, 2002 (Act No 17 of 2002) » National Conventional Arms Control Act, 2002 (Act No 41 of 2002) » National Environmental Management Act, 1998 (Act No 107 of 1998) » National Road Traffic Act, 1996 (Act No 93 of 1996) » National Strategic Intelligence Act, 1994 (Act No 39 of 1994) » Non-proliferation of Weapons of Mass Destruction Act, [...]

5. **Crime in South Africa - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Crime_in_South_Africa
   Content: | 2001 | 16.1 | 30.2 | 29.6 | 54.8 | 54.1 | 34.2 | 57.0 | 76.2 | 55.2 | 47.8 | | 2002 | 13.2 | 30.7 | 33.1 | 52.7 | 53.3 | 35.2 | 56.5 | 79.5 | 52.1 | 47.4 | | 2003 | 12.9 | 25.9 | 30.4 | 40.4 | 48.8 | 30.5 | 53.9 | 63.1 | 48.6 | 42.7 | | 2004 | 13.8 | 23.9 | 31.9 | 38.1 | 41.6 | 30.7 | 51.1 | 58.7 | 48.6 | 40.3 | | 2005 | 12.9 | 22.8 | 25.4 | 36.4 | 38.8 | 29.5 | 49.9 | 59.2 | 53.2 | 39.6 | | 2006 | 13.9 | 24.4 | 24.8 | 38.1 | 40.8 | 32.2 | 50.4 | 60.7 | 52.6 | 40.5 | | 2007 | 12.9 | 24.3 | 23.6 | 38.3 | 38.9 | 29.7 | 47.0 | 58.6 | 51.1 | 38.6 | | 2008 | 14.2 | 25.5 | 23.3 | 37.5 | 34.6 | 33.3 | 46.9 | 43.3 | 50.2 | 36.4 | | 2009 | 14.3 | 21.8 | 22.2 | 33.8 | 29.3 | 33.1 | 41.3 | 41.1 [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_012 - Not Enough Evidence

#### Input
- **Claim:** Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `false`
- **Score:** `8`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say there’s no evidence for the 25,000 child-torture/rape photos claim.
- **Explanation:** PolitiFact states there is no evidence that a laptop previously belonging to Hunter Biden contains child pornography, and that the specific allegation originated on an anonymous internet forum (Source 1). FactCheck.org similarly says the “25,000 pics” meme provides no evidence and references the same baseless social-media claim (Source 3).
- **Confidence reason:** Multiple fact-checkers directly reject the specific allegation.
- **Claim verdicts:**
```json
[
  {
    "claim": "Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://dpaq.de/gXxW2": "contradicting",
  "https://www.politifact.com/article/2020/dec/30/10-most-popular-social-media-fact-checks-2020/": "contradicting",
  "https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/": "contradicting",
  "https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter": "neutral",
  "http://biggs.house.gov/media/in-the-news/hunter-biden-laptop-claims-5-fast-facts-you-need-know": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Fact-checking unproven claims about Hunter Biden and child pornography**
   URL: https://dpaq.de/gXxW2
   Content: #### If Your Time is short There is no evidence that a laptop previously belonging to Hunter Biden contains child pornography. The allegation originated on an anonymous internet forum that’s a known source of online disinformation. See the sources for this fact-check Two weeks until Election Day, social media is rife with attacks on Joe Biden’s son Hunter Biden. A New York Post story about a recovered computer hard drive led to attacks about the Biden son’s business dealings. Facebook and cable news have gone further to suggest new and unsupported theories about what’s on the hard drive. One text post says, "Hunter Biden had 25,000 pics of him torturing and raping children under age 10 [...]

2. **PolitiFact | 10 most popular social media fact-checks of 2020**
   URL: https://www.politifact.com/article/2020/dec/30/10-most-popular-social-media-fact-checks-2020/
   Content: (Screenshot from Prntly.com) Claim: Says President Barack Obama "waited six months to call swine flu an emergency after thousands died." Rating: False The Obama administration declared swine flu, or H1N1, a public health emergency six weeks before H1N1 was declared a pandemic. No H1N1 deaths had yet been recorded in the United States. ## 6. Fact-checking unproven claims about Hunter Biden and child pornography Claim: Says "Hunter Biden had 25,000 pics of him torturing and raping children under age 10 in China on his laptop." Rating: False There is no evidence that a laptop previously belonging to Hunter Biden contains child pornography. The allegation originated on an anonymous [...]

3. **Social Media Posts Dredge Up Baseless 'Child Trafficking' Conspiracy Theory - FactCheck.org**
   URL: https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/
   Content: Alex Jones, the conspiracy theorist behind InfoWars and the bogus notion that the Sandy Hook school shooting in 2012 was a hoax, posted a video Oct. 17 that carried the headline “Confirmed: Trump Has Footage Of Hunter Biden Raping And Torturing Little Girls — Set To Release.” The video quotes Rudy Giuliani, President Donald Trump’s personal attorney, claiming to have pictures of Hunter Biden “that I can’t describe, some of which are illegal.” The video has received more than 2.2 million views. Another Facebook post makes this graphic, baseless claim: “Hunter Biden had 25,000 pics of him torturing and raping children under 10 in China on his laptop!” This kind of nonsense is circulating [...]

4. **Hunter Biden laptop letter - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter
   Content: By May 2023, no evidence had publicly surfaced to support suspicions that the laptop was part of a Russian disinformation scheme. FBI investigators handling Hunter Biden's laptop quickly concluded in 2019 "that the laptop was genuinely his and did not seem to have been tampered with or manipulated". PolitiFact wrote in June 2021 that the laptop did belong to Hunter Biden, but did not demonstrate wrongdoing by Joe Biden. ## Details [edit] [...] 5. ^ Barrett, Devlin; Viser, Matt (June 23, 2023). "Whistleblower accounts show Hunter Biden's laptop had little role in IRS probe". The Washington Post.`{{cite news}}`: CS1 maint: deprecated archival service (link) 6. ^ Drobnic Holan, Angie; [...]

5. **Hunter Biden Laptop Claims: 5 Fast Facts You Need to Know | Congressman Andy Biggs**
   URL: http://biggs.house.gov/media/in-the-news/hunter-biden-laptop-claims-5-fast-facts-you-need-know
   Content: Who is Joshua Wilson? There is an FBI agent named Joshua Wilson who has been assigned to child pornography and abduction cases over the years. A sitting senator, Ron Johnson (R-Wisconsin), went on Fox News and speculated about what that mean for Hunter Biden. To be clear, though, it hasn't been definitively proven that the laptop belonged to Hunter Biden; it also hasn't been definitively proven that the subpoena relates to that laptop. Business Insider reported that the name on the back page of the subpoena appears to say Joshua Wilson and refer to the Wilmington Office. Although the Joshua Wilson who works for the FBI has worked on child pornography cases over the years, Mac Isaac [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_016 - Not Enough Evidence

#### Input
- **Claim:** You see the number today? 33.1 GDP. The biggest in the history of our country by almost triple, right? Almost triple. Now it’s very much bigger than any GDP we’ve ever had. You have to go back to the 1950s, and then it’s less than half. This is the greatest number, 33.1 percent.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The 33.1% figure is supported, but the “triple” and “greatest ever” comparisons are not.
- **Explanation:** Sources 1 and 3 support that U.S. GDP grew at a 33.1% annualized rate in Q3 2020. However, Source 2 and Source 3 explicitly dispute the implication that this means the economy is “almost triple” or “the biggest in history,” explaining the 33.1% is an annualized rate and that the actual Q3 growth was 7.4%, plus noting the rebound is from a much lower base. Source 4 and Source 5 provide GDP levels by year, but the provided excerpts do not establish the specific “almost triple” or “greatest number, 33.1 percent” comparisons claimed.
- **Confidence reason:** 33.1% is supported; other comparisons are not evidenced.
- **Claim verdicts:**
```json
[
  {
    "claim": "You see the number today? 33.1 GDP.",
    "verdict": "supported"
  },
  {
    "claim": "The biggest in the history of our country by almost triple, right? Almost triple.",
    "verdict": "contradicted"
  },
  {
    "claim": "Now it’s very much bigger than any GDP we’ve ever had.",
    "verdict": "unverifiable"
  },
  {
    "claim": "You have to go back to the 1950s, and then it’s less than half.",
    "verdict": "unverifiable"
  },
  {
    "claim": "This is the greatest number, 33.1 percent.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html": "supporting",
  "https://enewspaper.latimes.com/infinity/article_share.aspx?guid=b4a6e8b2-c9dd-4f7f-9c93-08cf03222a7e": "contradicting",
  "https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068": "contradicting",
  "https://www.multpl.com/us-gdp-inflation-adjusted/table/by-year": "neutral",
  "https://www.macrotrends.net/3004/us-gdp": "neutral"
}
```

#### Search Evidence Input
1. **U.S. GDP booms at 33.1% rate in Q3 report, beating expectations**
   URL: https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html
   Content: "This is going to be seized upon by both ends of the political spectrum as either evidence of the strength of the post-lockdown economic rebound or a cursory warning that the gains could be short-lived," said James McCann, senior global economist at Aberdeen Standard Investments. "The reality is that the GDP numbers demonstrate that the U.S. economy did indeed rebound strongly as lockdown measures were lifted." In a tweet, Trump noted the "Biggest and Best in the History of our Country" GDP number and said growth in 2021 will be "FANTASTIC!!!" For his part, Biden noted that while the economy improved "visits to food banks haven't slowed, and poverty has grown." [...] CNBC Join IC Join [...]

2. **Record growth is no reason for Trump to brag**
   URL: https://enewspaper.latimes.com/infinity/article_share.aspx?guid=b4a6e8b2-c9dd-4f7f-9c93-08cf03222a7e
   Content: Trump took out advance advertisements on Facebook even before the release, according to the Financial Times, bragging that the GDP number would be “the highest in American history.” He should put a sock in it. Here’s why. First, the headline number of 33.1% is intrinsically misleading — it’s an annualized rate, meaning that it’s how fast the economy would grow if the actual third-quarter figures were extended out to a whole year. In truth, the economy grew by only 7.4% in the third quarter. Moreover, either way you take it — whether as an annualized rate or the actual GDP change for the quarter — it must be considered in the context of previous changes in the size of the economy. [...] [...]

3. **GDP rose at 33.1 percent annualized rate last quarter, but blowout figure is not what it seems**
   URL: https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068
   Content: Vice President Mike Pence echoed Trump’s self-congratulations in a tweet of his own, saying, “President @realDonaldTrump created the Greatest economy in the history of the world and we are well on our way back to that with today’s amazing Third Quarter GDP number!” In reality, a polarized electorate and worry about Trump’s handling of the pandemic make this bounceback less significant than it might otherwise have been, and market observers say the inability to contain Covid-19 makes this economic growth tenuous. “It’s easier to get big growth rates when you're coming off a lower base. That’s what a lot of this is,” said Dan North, senior economist at Euler Hermes North America. [...] [...]

4. **US Real GDP by Year - Multpl**
   URL: https://www.multpl.com/us-gdp-inflation-adjusted/table/by-year
   Content: | Dec 31, 1959 | 3.44 trillion | | Dec 31, 1958 | 3.29 trillion | | Dec 31, 1957 | 3.20 trillion | | Dec 31, 1956 | 3.19 trillion | | Dec 31, 1955 | 3.13 trillion | | Dec 31, 1954 | 2.94 trillion | | Dec 31, 1953 | 2.86 trillion | | Dec 31, 1952 | 2.84 trillion | | Dec 31, 1951 | 2.70 trillion | | Dec 31, 1950 | 2.56 trillion | | Dec 31, 1949 | 2.26 trillion | | Dec 31, 1948 | 2.29 trillion | | Dec 31, 1947 | 2.21 trillion | | Dec 31, 1946 | 2.21 trillion | | Dec 31, 1945 | 2.50 trillion | | Dec 31, 1944 | 2.52 trillion | | Dec 31, 1943 | 2.34 trillion | | Dec 31, 1942 | 2.00 trillion | | Dec 31, 1941 | 1.68 trillion | | Dec 31, 1940 | 1.43 trillion | | Dec 31, 1939 | 1.31 trillion | | [...]

5. **U.S. GDP (1947-2025)**
   URL: https://www.macrotrends.net/3004/us-gdp
   Content: ## U.S. GDP (1947-2025) Markets Metals Energy Commodities Interest Rates Exchange Rates Economy Inflation Rate Unemployment National Debt Debt/GDP Housing Starts Initial Claims Retail Sales Industrial Prod Durable Goods # U.S. GDP: $31.423T as of December 2025. ###### Units: Dollars ###### Frequency: Quarterly ###### Release: Gross Domestic Product ###### Source: U.S. Bureau of Economic Analysis ## Historical Chart | Related Charts | [...] ## Historical Chart | Related Charts | | U.S. Real GDP | | U.S. Real GDP Per Capita | | GDPNow Model Estimate | | U.S. Gross National Product | | U.S. Real GDP | | Real Potential GDP | | St. Louis Fed Real GDP Nowcast | | Real GNP | | GDP per Capita [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_017 - Supported

#### Input
- **Claim:** Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true, mostly_true`
- **TLDR:** Sources do not support a specific loss of 300,000 manufacturing jobs from the trade war.
- **Explanation:** Source 1 mentions Moody’s estimating the trade conflict with China has reduced U.S. employment by 300,000 jobs, but it does not specify that these are manufacturing jobs. Source 3 instead reports economy-wide job losses (245,000 jobs) and finds tariffs reduced manufacturing employment (1.4%), which contradicts the claim’s specific figure and manufacturing-job framing. Source 2 finds no evidence of net U.S. job losses from the “China shock” overall, further undermining the claim.
- **Confidence reason:** Only one source mentions 300,000, and it’s not clearly manufacturing jobs.
- **Claim verdicts:**
```json
[
  {
    "claim": "Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.statesman.com/story/news/politics/elections/2020/07/01/fact-check-did-trump-lose-trade-war-that-he-started-per-biden-ad/113740186/": "neutral",
  "https://sccei.fsi.stanford.edu/china-briefs/did-china-shock-cause-widespread-job-losses-us": "contradicting",
  "https://econofact.org/factbrief/did-the-trump-tariffs-increase-us-manufacturing-jobs": "contradicting",
  "https://www.cato.org/blog/manufacturing-employment-data-confirms-concentrated-benefits-dispersed-costs-trumps-tariffs": "neutral",
  "https://www.progressivepolicy.org/u-s-manufacturing-employment-is-down-108000-in-2025/": "neutral"
}
```

#### Search Evidence Input
1. **Fact-check: Did Trump lose a trade war that he started, per Biden ad?**
   URL: https://www.statesman.com/story/news/politics/elections/2020/07/01/fact-check-did-trump-lose-trade-war-that-he-started-per-biden-ad/113740186/
   Content: "U.S. tariffs against Chinese manufactured imports disrupted U.S. supply chains, raising input costs to many U.S. firms that used these products," Jones said. Independent observers have projected a net economic hit to the United States from the trade friction with China. A 2019 study by the Organization for Economic Cooperation and Development estimated that the tariff hikes could cut U.S. and Chinese GDP by 0.9% and 1.1%, respectively, by 2021-22. In a December 2019 study, Federal Reserve researchers concluded that Trump's tariffs "have not boosted manufacturing employment or output, even as they increased producer prices." And the economic analysis firm Moody's concluded in September [...]

2. **Did the “China Shock” Cause Widespread Job Losses in the U.S.? | FSI**
   URL: https://sccei.fsi.stanford.edu/china-briefs/did-china-shock-cause-widespread-job-losses-us
   Content: No evidence of net U.S.job losses resulting from China shock. Increasing import competition from China reallocated jobs and earnings from manufacturing in the U.S. heartland to the service sector in coastal urban areas. Researchers do not find evidence of net job loss, however, in the U.S. as a whole between 1990 and 2014. One-third of manufacturing job losses were caused by existing businesses that repurposed their operations from manufacturing to services, particularly in research, management, and wholesale.Large multinational firms were the primary drivers of manufacturing job losses, switching into research, design, management, wholesale, and other service sectors. Plants operating [...]

3. **Fact Check: Did the Trump tariffs increase US manufacturing jobs? | Econofact**
   URL: https://econofact.org/factbrief/did-the-trump-tariffs-increase-us-manufacturing-jobs
   Content: Economy-wide, Oxford Economics estimated in 2021 that the tariffs and resulting trade war cost 245,000 jobs and 0.5% of GDP while reducing real incomes by $675 per household. This fact brief is responsive to conversations such as this one. ### Sources: EconoFact The U.S. and China: Trade and Trade Wars Federal Reserve Board Disentangling the Effects of the 2018-2019 Tariffs on a Globally Connected U.S. Manufacturing Sector FRED (Federal Reserve Bank Of St. Louis) All Employees, Manufacturing (MANEMP) Progressive Policy Institute Trade Fact of the Week: Trump-era tariffs raised prices but did not ‘bring manufacturing back’ Oxford Economics The US-China Economic Relationship [...] The [...]

4. **Manufacturing Employment Data Confirm the Concentrated Benefits—and Dispersed Costs—of Trump’s Tariffs | Cato at Liberty Blog**
   URL: https://www.cato.org/blog/manufacturing-employment-data-confirms-concentrated-benefits-dispersed-costs-trumps-tariffs
   Content: Survey evidence reinforces this conclusion. For instance, the December 2025 ISM Manufacturing Purchasing Manager’s Index, a widely watched measure of the US factory activity based on a monthly survey of supply chain executives, fell to 47.9—the lowest reading of the year and the sector’s tenth consecutive month of contraction. (Above 50 indicates expansion; below 50 indicates contraction.) In fact, the reading was the lowest of 2025. The PMI’s sub-indices tracking orders and prices, as well as testimonies offered by the surveyed executives, repeatedly point to higher input costs and trade policy uncertainty driven by the administration’s tariff regime as key headwinds.

5. **U.S. manufacturing employment is down 108,000 in 2025**
   URL: https://www.progressivepolicy.org/u-s-manufacturing-employment-is-down-108000-in-2025/
   Content: “Damage is done when a consumer who would have benefited from a $30 toaster chooses not to buy one for $33. A second cost appears as consumers switch to domestic options that are more expensive. The consumer who buys the $32 toaster made in America pays the extra $2, but the government collects no extra revenue. Still, the share of the $32 purchase price that would once have gone to a Chinese factory and its workers now goes to an American firm and its workers instead. It pays American taxes and supports American families in American communities.” [...] Ed Gresser Trade Fact | April 8, 2026 ### U.S. Customs blocks about $0.8 billion worth of goods a year on suspicion of ‘forced labor’ [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_018 - Not Enough Evidence

#### Input
- **Claim:** There was a 40% drop in the price of oil, Nigeria's main export.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources support a 40% export drop, not a 40% oil price drop.
- **Explanation:** Source 1 says Nigeria’s exports fell about 40.3% (2015 vs 2014) and that crude oil exports declined sharply, but it does not state that the *price of oil* dropped by 40%. Sources 2 and 3 discuss oil prices falling below $40, but they provide no 40% figure for the oil price drop. Therefore, the “40% drop in the price of oil” part is not supported by the provided sources.
- **Confidence reason:** Oil-price magnitude not given; export drop is quantified.
- **Claim verdicts:**
```json
[
  {
    "claim": "There was a 40% drop in the price of oil, Nigeria's main export.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.tralac.org/news/article/9314-nigerian-exports-slumped-40-last-year-as-oil-prices-plunged.html": "supporting",
  "https://cpeel.ui.edu.ng/news/oil-prices-below-40-what-it-means-nigeria-local-oil-companies-banks": "neutral",
  "https://www.arise.tv/fresh-concerns-in-nigeria-as-crude-oil-price-slumps-below-40/": "neutral",
  "https://assets.publishing.service.gov.uk/media/57a08a4b40f0b6497400051e/61062Case-Study-Nigeria.pdf": "neutral",
  "https://www.legit.ng/business-economy/money/1703251-new-data-shows-buying-50-crude-oil-nigeria/": "neutral"
}
```

#### Search Evidence Input
1. **Nigerian exports slumped 40% last year as oil prices plunged - tralac trade law centre**
   URL: https://www.tralac.org/news/article/9314-nigerian-exports-slumped-40-last-year-as-oil-prices-plunged.html
   Content: The value of the nation’s exports totalled N2,076.7 billion in Q4, 2015, showing a decrease of N256.5billion, or 11.0%, over the value recorded in the preceding quarter. On an annual basis total exports from Nigeria stood at N9,728.8 billion at the end of 2015, representing a drop of N6,575.2 billion or 40.3% over levels recorded in 2014. Notwithstanding a steep decline in crude oil exports by N4,945.9 billion or 41.6% in 2015, the structure of Nigeria’s exports is still dominated by crude oil exports. The contribution of crude oil to the value of total domestic export trade amounted to N6,945.3 billion or 71.4% in 2015 (estimate figures). [...] Exports by Section, revealed that the [...]

2. **Oil Prices Below $40: What it Means for Nigeria, Local Oil Companies, Banks | Centre for Petroleum, Energy Economics & Law**
   URL: https://cpeel.ui.edu.ng/news/oil-prices-below-40-what-it-means-nigeria-local-oil-companies-banks
   Content: Energy News 18 September 2020 The price of Brent, the benchmark of Nigeria’s crude oil has fallen to $39 as bearish factors mount and sentiment shifts add another wrench in the recovery for oil prices still reeling from the pandemic-driven blow to consumption. Brent futures dropped 4.1 percent to $38.95 a barrel as at 2 pm Nigerian Time, while US crude dropped by 1.10 percent, to $37.67. One major factor behind the fall in oil price is the concerns over rising exports from the Organisation of Petroleum Exporting Countries (OPEC) and allies’ in third quarter of 2020, with the possibility of a total breakdown of the OPEC+ agreement.

3. **Fresh Concerns in Nigeria as Crude Oil Price Slumps below $40**
   URL: https://www.arise.tv/fresh-concerns-in-nigeria-as-crude-oil-price-slumps-below-40/
   Content: “Nigerian exports to the United States are dominated by crude oil, which at $4.4 billion, accounted for 88% of US imports from Nigeria in 2019. According to US International Trade Commission data, Nigeria consistently ranks as the top source of exports to the United States under the African Growth and Opportunity Act,” it stated However, it noted that Nigeria also remains a major regional destination for US exports of motor vehicles and refined petroleum products (e.g., gasoline), which are among the fastest-growing U.S. exports to Africa. Agricultural products and machinery, the research group said, are other top US exports to the country, adding that Nigeria’s demand also has driven [...]

4. **[PDF] Oil Shock Vulnerabilities & Impacts: Nigeria Case Study - GOV.UK**
   URL: https://assets.publishing.service.gov.uk/media/57a08a4b40f0b6497400051e/61062Case-Study-Nigeria.pdf
   Content: top net exporters of crude oil, it is nonetheless heavily reliant on imports of refined fuels, which are essential to the functioning of its economy. This poses a risk to the domestic economy in the event of global oil and refined fuel shortages in the future. -40% -30% -20% -10% 0% 10% 20% 30% 1981 1983 1985 1987 1989 1991 1993 1995 1997 1999 2001 2003 2005 2007 2009 2011 production consumption 17 Figure 16: Nigeria’s net oil exports, 1986-2009 Source: EIA, 2012a. 3.4 Conflict over access to oil wealth Poverty and inequality in the distribution of oil wealth in Nigeria has led to widespread oil bunkering, which refers to the theft and trade in stolen oil. According to EIA (2012b), [...]

5. **New Data Shows US Buying 50% Less Crude Oil From Nigeria - Legit.ng**
   URL: https://www.legit.ng/business-economy/money/1703251-new-data-shows-buying-50-crude-oil-nigeria/
   Content: ## Another African country leads Despite the decline, crude oil remains Nigeria’s dominant export to the United States, accounting for about 63% to 65% of total US imports from the country in January. Total US imports from Nigeria fell to $183 million from $297 million in December, reflecting the broader contraction in trade flows. At the same time, the United States recorded a goods trade surplus of $419 million with Nigeria, widening sharply from $84 million in December as exports to Nigeria rose to $602 million. Across Africa, however, the US posted a trade deficit of $503 million, reversing a surplus recorded in the previous month. Nigeria’s crude export value to the US falls [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_020 - Supported

#### Input
- **Claim:** Edo State in Nigeria has a 19% unemployment rate.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** Sources don’t provide enough direct evidence that Edo’s unemployment rate is 19%.
- **Explanation:** Source 1 reports Obaseki’s claim that Edo’s unemployment fell from 25% to 19% and says it is “verifiable with” an NBS report, but it does not reproduce the NBS state figure itself. The other sources provided do not give Edo’s unemployment rate of 19% (Source 2 discusses unemployment generally and mentions 2024 national unemployment, Source 3 focuses on national unemployment, and Source 5 is an NBS page for Q3 2018 without the 19% figure).
- **Confidence reason:** Only one source mentions 19% for Edo; NBS figure not shown.
- **Claim verdicts:**
```json
[
  {
    "claim": "Edo State in Nigeria has a 19% unemployment rate.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/": "supporting",
  "https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf": "neutral",
  "https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/": "neutral",
  "https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria": "neutral",
  "https://www.nigerianstat.gov.ng/elibrary/read/929": "neutral"
}
```

#### Search Evidence Input
1. **Is Edo unemployment rate 19 percent as claimed by Obaseki? - Dubawa**
   URL: https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/
   Content: Excerpt of Obaseki’s statement. ### Verification A keyword search by Dubawa showed that in August 2020, a report by The Nation indicates that the unemployment rate in Edo state has reduced to 19%. The report which quoted a Nigeria Bureau of Statistics (NBS) report, noted Edo State has the lowest unemployment figure in the South-South region, compared to five other oil-rich states in the region. Is Edo unemployment rate 19 percent as claimed by Obaseki? [...] Channels Television had earlier conducted a poll which allowed the public to choose two candidates they would love to appear in the debate. The candidates of the APC and PDP emerged top of the poll. During the governorship debate [...]

2. **[PDF] perception of edo residents towards unemployment**
   URL: https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf
   Content: 10 Unemployment is one of the fundamental developmental challenges facing Nigeria at the moment. Research have shown that unemployment was rapid in the 1980s but the obtainable report from diverse local and international bodies and the glaring evidence of joblessness in these decades are clear evidences that there was no time in Nigeria’s checkered history where unemployment is as serious as now (Asaju et al, 2014) In previous days, the eventuality of unemployment though present, was not on a high rise where a high number of educated individuals roam the streets of the country, jobless. [...] 2.2.1 Unemployment in Nigeria “Educated and unemployed” is the raised placard in Nigeria as [...]

3. **How true are viral claims on Nigeria’s unemployment rate, extreme poverty and debt profile? | The ICIR- Latest News, Politics, Governance, Elections, Investigation, Factcheck, Covid-19**
   URL: https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/
   Content: The tweet read: “\ 28% unemployment rate, \ 49% in extreme poverty, \ $85.9Bn debt and counting, Buhari just approved N10 billion for census. Extreme irresponsible behavior is main crisis facing leadership in Nigeria.” THE CLAIMS: From the tweet, these claims were established: THE FINDINGS: Claim 1: The FactCheckHub first checked the National Bureau of Statistics (NBS) website for the data on Nigeria’s labour statistics to determine the total percentage of unemployment rate in the country. According to the statistics on Nigeria’s labour force released by the NBS for 2nd quarter (Q2) of 2020, Nigeria currently has 21,764,617 unemployed people. The data also stated that 27.1% people are [...]

4. **12 Unemployment Statistics in Nigeria for 2026 | MyJobMag**
   URL: https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria
   Content: A state-by-state breakdown was given, with Abia State recording the highest rate of unemployment at 18.7%, followed by the FCT and Rivers State with 14.1% and 13.4% respectively. Borno reported the least amount with 7.3% of the citizenry unemployed. The unemployment rate fell to 4.3% in Q2 2024, reversing a rising trend since Q2 2023. Also, the educational distribution of Nigerians played a major role in their employability. Persons with tertiary education had a higher employment rate compared to others in the educational subset. Despite the drop in unemployment, Nigeria's misery index (the sum of unemployment and inflation rate) rose to 38.3% in Q2 2024. This marks an increase from [...]

5. **Reports | National Bureau of Statistics**
   URL: https://www.nigerianstat.gov.ng/elibrary/read/929
   Content: Coat of Arm Nigeria Flag ## Labor Force Statistics - Volume 2: Unemployment and Underemployment by State (Q3 2018) ## Labor Force Statistics - Volume 2: Unemployment and Underemployment by State (Q3 2018) ### Summary - Unemployment and Underemployment rates vary across states according to the nature of economic activity predominant in each State. States with higher focus on seasonal agriculture tend to have higher rates of underemployment compared to unemployment. This may swing from high full-time employment during periods of planting and harvest, when they are fully engaged on their farms, to periods of high underemployment and even unemployment at other periods in between.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_021 - Not Enough Evidence

#### Input
- **Claim:** Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `20`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** TheCable’s calculations indicate Saudi petrol was more expensive than Nigeria, contradicting the claim.
- **Explanation:** Source 1 (TheCable Fact Check) calculates that Saudi Arabia’s petrol prices were 17.78% (octane 95) and 11.16% (octane 91) more expensive than Nigeria’s after currency conversion, which contradicts the claim that Nigeria’s 2020 fuel was not cheaper than Saudi Arabia. The other sources either don’t provide comparable 2020 price data (Sources 2 and 3) or discuss Saudi fuel prices generally without Nigeria-2020 comparison (Sources 4 and 5).
- **Confidence reason:** Only one source directly compares Nigeria vs Saudi prices with calculations.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/": "supporting",
  "https://www.facebook.com/groups/599563341561133/posts/1445300556987403/": "neutral",
  "https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/": "neutral",
  "https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf": "neutral",
  "https://tradingeconomics.com/country-list/gasoline-prices": "neutral"
}
```

#### Search Evidence Input
1. **FACT CHECK: Is petrol 40% cheaper in Nigeria than in Saudi Arabia as claimed by Dangote? - TheCable Fact Check**
   URL: https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/
   Content: On the other hand, on September 3, the Nigerian National Petroleum Company (NNPC) Limited increased thepetrol price across its retail outlets to N855 per litre. After converting the riyal value to naira, the naira denomination was used to determine the difference between petrol prices in both countries. As a result, Saudi Arabia’s petrol is 17.78 percent (for octane 95 petrol) and 11.16 percent (for octane 91 petrol), respectively, more expensive than that of Nigeria. Moreover, converting the petrol prices of both countries to dollars would lead to a similar result which is way less than the 40 percent Dangote claimed. Verdict: Partly false. The claim that petrol costs 40 percent less [...]

2. **Fuel price comparison between Saudi Arabia and Nigeria - Facebook**
   URL: https://www.facebook.com/groups/599563341561133/posts/1445300556987403/
   Content: Now, a Nigerian can only buy 73 Litres of fuel with his minimum wage, while a Saudi Arabian will buy about 1,717 Litres of fuel. The difference.

3. **FG justifies fuel price comparison with Saudi Arabia, others | Multiplatform Digital Information Technology**
   URL: https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/
   Content: President Buhari said in his Independence Day broadcast that: “we sell petrol at N161 per litre when same is sold at N168 per litre in Saudi Arabia; N211 per litre in Egypt; N362 per litre in Ghana; N362 per litre in Chad, and N346 per litre in Niger Republic. “It does not make sense for petrol to be cheaper in Nigeria than Saudi Arabia,’’ ## READ ALSO: ONDO DECIDES: APC accuses PDP, ZLP of creating tension ahead of polls A cross section of Nigerians, however, criticised the president for making such comparison without considering the minimum wage, standard of living and infrastructure in Saudi Arabia in particular. Responding to the critics, the minister said there was nothing wrong [...]

4. **[PDF] Fossil fuel subsidy swaps: A path towards accelerating the ...**
   URL: https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf
   Content: can be rightly ascribable to the decline in energy prices fueled by the rise in fossil fuel subsidies. Fuel prices in Saudi Arabia are amongst the lowest in the entire world: Gasoline, for example, costs only 62 cents per liter, while its global price is $2.54 per liter (Bloomberg, 2024). This relatively huge gap between domestic and international prices represents foregone revenue and could be viewed as an implicit subsidy (Aldubyan and Gasim, 2021). Hartley and Medlock III (2008) report that Saudi citizens believe they deserve low energy prices as a way to take advantage of their country's fossil fuel wealth. On account of the high, subsidy-driven energy consumption, population [...]

5. **Gasoline Prices - Countries - List**
   URL: https://tradingeconomics.com/country-list/gasoline-prices
   Content: | Country | Last | Previous | Reference | Unit | --- --- | Indonesia | 0.59 | 0.6 | Mar/26 | USD/Liter | | Saudi Arabia | 0.62 | 0.62 | Mar/26 | USD/Liter | | Russia | 0.83 | 0.87 | Mar/26 | USD/Liter | | United States | 0.96 | 0.77 | Mar/26 | USD/Liter | | India | 1.01 | 1.04 | Mar/26 | USD/Liter | | Japan | 1.11 | 1.01 | Mar/26 | USD/Liter | | Argentina | 1.19 | 1.11 | Mar/26 | USD/Liter | | South Africa | 1.2 | 1.26 | Mar/26 | USD/Liter | | South Korea | 1.23 | 1.18 | Mar/26 | USD/Liter | | Canada | 1.28 | 1.02 | Mar/26 | USD/Liter | | Brazil | 1.29 | 1.23 | Mar/26 | USD/Liter | | Mexico | 1.35 | 1.35 | Mar/26 | USD/Liter | | China | 1.37 | 1.03 | Mar/26 | USD/Liter | | Turkey | [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_022 - Refuted

#### Input
- **Claim:** The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No provided source shows Nigeria donating $600M to Biden’s campaign.
- **Explanation:** None of the sources state that the Nigerian government donated $600 million to Joe Biden’s campaign. Source 1 discusses $600 million in unemployment funds allegedly siphoned by Nigerian scammers, and mentions Biden donors, but not a Nigerian government donation to Biden’s campaign. Sources 2, 3, 4, and 5 discuss other foreign donations or U.S. assistance efforts, without supporting the specific claim about a $600 million Nigerian government donation to Biden’s campaign.
- **Confidence reason:** Only tangentially related information; no direct evidence for the $600M donation claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/": "neutral",
  "https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues": "neutral",
  "https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-": "neutral",
  "https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/": "neutral",
  "https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf": "neutral"
}
```

#### Search Evidence Input
1. **Biden pick for unemployment program lost $600M to Nigerian scammers**
   URL: https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/
   Content: The Seattle Times described her as a “potent, behind-the-scenes force in Democratic politics” and said she had entertained a string of 2020 presidential candidates in salon-style fundraisers at her home. The newspaper’s analysis of federal campaign records found she and her husband Eric donated more than $400,000 to the Biden campaign and other Democratic causes in the past two years. The Department of Labor and the White House did not respond to requests for comment. ### Tag: # Magazine Magazine Covers # More from News [...] Logo Logo # Biden pick for unemployment program lost $600M to Nigerian scammers Biden pick for unemployment program lost $600M to Nigerian scammers President [...]

2. **Trump wants to investigate Democrats' fundraising, but his own campaign has issues | PBS News**
   URL: https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues
   Content: Regulators and watchdogs have also long been concerned about donations from individuals with ties to foreign interests. Trump has received many such contributions, including one in December from Nnenna Peters, the wife of Benedict Peters, a Nigerian billionaire who is the founder and CEO of oil and mining businesses. Nnenna Peters, who goes by Ella, gave $1 million to Trump's inaugural committee. A naturalized citizen, Nnenna Peters — who lives in Potomac, Maryland, a tony suburb of the capital — is allowed to make campaign donations. [...] Benedict Peters, as it turns out, has a lot to offer that could be of interest to Trump, who has made the extraction of natural resources a focus [...]

3. **FACT SHEET: U.S. Efforts to Assist the Nigerian Government in its Fight against Boko Haram | whitehouse.gov**
   URL: https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-
   Content: Jump to main content Jump to navigation Home ## Search form ## You are here ## Briefing Room # FACT SHEET: U.S. Efforts to Assist the Nigerian Government in its Fight against Boko Haram [...] Boko Haram is inflicting untold hardship on the people of Nigeria, with repercussions for men, women, girls, and boys throughout northeast Nigeria. The United States provides assistance to affected populations, including support to health, water, and sanitation services; the delivery of emergency relief supplies; and protection services, including psycho-social support for survivors of Boko Haram violence. The United States further invests in helping Nigeria to build security and increase [...]

4. **KOCO 5 News**
   URL: https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/
   Content: # KOCO 5 News - A report from the State Department lists... | Facebook Log In Log In Forgot Account? ## KOCO 5 News's Post []( ### KOCO 5 News January 29 · A report from the State Department lists tens of thousands of dollars in foreign gifts to former President Joe Biden and other officials in the last year of the Biden administration. Image 1: May be an image of text that says 'BIDEN'S FOREIGN GIFTS STATE DEPARTMENT REPORT DETAILS FOREIGN GIFTS GIVEN tO JOE BIDEN IN 2024' Image 2 Image 3 Image 4 All reactions: 665 956 comments 62 shares Like Comment Most relevant Taylor States Like a plane? 12w 356 Image 5 View all 46 replies Lydia C Willis And he sent them to the national archives. [...]

5. **[PDF] Congress Must Stop Biden's Misuse of U.S. Foreign Aid to Impose ...**
   URL: https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf
   Content: A review of the first 50 USAID employees, chosen alphabetically, who made political contributions during the 2020 federal election cycle shows that 48 of them donated to Democratic candidates and causes, with just two giving to Republicans, a 12 to 1 ratio. Of the estimated $48,000 donated, only $600 went to Republicans, less than 2 percent of the total.REF Following the slaying of George Floyd in late May 2020, an election year, over 1,000 USAID staff demanded that the agency “make a public statement affirming that Black Lives Matter,” accused USAID “of structural racism,” and insisted USAID design a plan to address “systemic injustice, racism, colonialism, and police brutality,” [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. AVeriTeC / av_027 - Refuted

#### Input
- **Claim:** The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `true`
- **Score:** `95`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `true`, expected one of `false, mostly_false`
- **TLDR:** The claim is debunked: PIB and other fact-checkers say no such shootdown occurred.
- **Explanation:** All provided sources state the viral allegation is fake and that no incident of the PLA shooting down an IAF Su-30 in Tibet took place. Newschecker (Source 1) says PIB debunked the claim as fake, Latestly (Source 2) reports PIB’s denial, and Vishvas News (Source 5) adds that IAF denied it and no such incident was found.
- **Confidence reason:** Multiple fact-check sources directly debunk the shootdown claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://newschecker.in/fact-check/pla-did-not-shoot-down-indian-fighter-jet-sukhoi-su-30-in-tibet": "contradicting",
  "https://www.latestly.com/social-viral/fact-check/iaf-sukhoi-su-30-fighter-jet-was-not-shot-down-by-chinas-pla-in-tibet-pib-debunks-fake-news-2066857.html": "contradicting",
  "https://www.instagram.com/p/CF6t5R3DEn8/": "contradicting",
  "https://x.com/PIBFactCheck/status/1312692937898119169": "contradicting",
  "https://www.vishvasnews.com/english/politics/fact-check-iafs-sukhoi-30-jet-was-not-shot-down-in-tibet-viral-claim-is-fake/": "contradicting"
}
```

#### Search Evidence Input
1. **PLA Did Not Shoot Down Indian Fighter Jet Sukhoi Su–30 In Tibet - Newschecker**
   URL: https://newschecker.in/fact-check/pla-did-not-shoot-down-indian-fighter-jet-sukhoi-su-30-in-tibet
   Content: Claim: A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot down by PLA Air Force in #Tibet.#PIBFactCheck: The claim is #FAKE. No such incident has taken place. pic.twitter.com/SFHUTYiOsD The Press Information Bureau in Jharkhand debunked this claim as well. Claim: A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot down by PLA Air Force in #Tibet.#PIBFactCheck: The claim is #FAKE. No such incident has taken place. pic.twitter.com/Aw1ZapUAEK This claim is shared at a time when territorial disputes between India and China in Ladakh continue. ### Previous Claims Made By The User The user in context, Zhong Xin (@ZhongXN), claims to be a columnist based in China [...]

2. **IAF Sukhoi Su-30 Fighter Jet Was Not Shot Down by China's PLA in Tibet; PIB Debunks Fake News | 🔎 LatestLY**
   URL: https://www.latestly.com/social-viral/fact-check/iaf-sukhoi-su-30-fighter-jet-was-not-shot-down-by-chinas-pla-in-tibet-pib-debunks-fake-news-2066857.html
   Content: See Zhong Xin's Tweet Breaking News: Our Air force has shutdown Indian fighter jet Sukhoi su–30 in Tibet. — Zhong Xin 🇨🇳 (@ZhongXN) October 3, 2020 Fact-Check: Press Information Bureau (PIB), the Indian government's official meida arm, debunked the fake news. The fact-check handle of PIB on Twitter informed netizens that the tweet posted Zhong Xin and shared by several microbloggers is absolutely untrue. PIB Fact Check Debunks Fake News Claim: A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot down by PLA Air Force in #Tibet.#PIBFactCheck: The claim is #FAKE. No such incident has taken place. pic.twitter.com/SFHUTYiOsD — PIB Fact Check (@PIBFactCheck) October 4, 2020 [...]

3. **Instagram**
   URL: https://www.instagram.com/p/CF6t5R3DEn8/
   Content: Claim: A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot down by PLA Air Force in #Tibet. #PIBFactCheck: The claim is #FAKE. No

4. **A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot ...**
   URL: https://x.com/PIBFactCheck/status/1312692937898119169
   Content: Claim: A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot down by PLA Air Force in #Tibet. #PIBFactCheck: The claim is #FAKE.

5. **Fact Check: IAF’s Sukhoi-30 jet shot down in Tibet? No, viral claim is fake**
   URL: https://www.vishvasnews.com/english/politics/fact-check-iafs-sukhoi-30-jet-was-not-shot-down-in-tibet-viral-claim-is-fake/
   Content: ## subscribe Subscribe to our newsletter and get exclusive fact checking news everyweek ## subscribed Thank you You are now subscribed to our newsletter # Fact Check: IAF’s Sukhoi-30 jet was not shot down in Tibet, viral claim is fake The viral post that China has shot down IAF fighter jet’s Sukhoi – 30 in Tibet is fake. IAF has denied the viral claim. New Delhi (Vishvas News):A viral post on social media claims that China has shot down Indian Air force (IAF) fighter jet’s Sukhoi SU-30. We found this was shared as breaking news first on Twitter and then on Facebook. Vishvas News investigation revealed the claim is fake. IAF has denied such claims. Claim [...] #WATCH: Indian Air Force [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. PolitiFact / pf_002 - false

#### Input
- **Claim:** Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false, mostly_false`
- **TLDR:** Sources say the Wisconsin Supreme Court ended the John Doe investigation, but not that it was a resolved “criminal investigation.”
- **Explanation:** WPR and EXPOSEDbyCMD both state that the Wisconsin Supreme Court ended the John Doe investigation and explicitly said it “ends the John Doe investigation” (WPR). EXPOSEDbyCMD also describes the court shutting down the John Doe investigation and ordering documents destroyed/returned. However, none of the provided sources clearly support the specific framing that it was a “secret John Doe criminal investigation of his campaign” resolved by “two judges” saying it is over; they discuss a 4-2 decision and multiple justices, not two judges making that statement.
- **Confidence reason:** Multiple sources confirm termination, but “two judges” and “criminal” framing aren’t directly supported.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.exposedbycmd.org/2016/09/22/leaked-documents-court-dismissal-john-doe-false-premise/": "supporting",
  "https://www.wpr.org/politics/state-supreme-court-ruling-blocks-john-doe-probe": "supporting",
  "https://www.theguardian.com/us-news/2016/sep/14/corporate-cash-john-doe-files-scott-walker-wisconsin": "neutral",
  "https://www.motherjones.com/politics/2007/07/search-john-doe-no-2-story-feds-never-told-about-oklahoma-city-bombing/": "neutral",
  "https://www.exposedbycmd.org/2016/06/23/cmd-urges-u-s-supreme-court-to-hear-prosecutors-appeal-in-john-doe-ii-corruption-case/": "supporting"
}
```

#### Search Evidence Input
1. **Leaked Documents Show Court's Dismissal of the John Doe Was Based on a False Premise - EXPOSEDbyCMD**
   URL: https://www.exposedbycmd.org/2016/09/22/leaked-documents-court-dismissal-john-doe-false-premise/
   Content: In a controversial ruling that July, the Court voted 4-2 to shut down the John Doe investigation into Scott Walker’s secret political fundraising scheme, arguing that coordination between Walker, his campaign consultants, and corporate lobby groups didn’t matter because it was all just “issue advocacy.” When the special prosecutor moved for reconsideration later that year, presenting evidence of express political advocacy, the court’s conservative majority, led by Justice Gableman, promptly fired him. It was Wisconsin’s version of the Saturday Night Massacre, when Richard Nixon had Archibald Cox canned (by Robert Bork) as the special prosecutor in the Watergate scandal. [...] The [...]

2. **State Supreme Court Ruling Blocks John Doe Probe - WPR**
   URL: https://www.wpr.org/politics/state-supreme-court-ruling-blocks-john-doe-probe
   Content: # State Supreme Court Ruling Blocks John Doe Probe Investigation Looked Into Allegations Of Coordination Between Candidates, Groups The Wisconsin Supreme Court has ended a long-running John Doe investigation into whether Gov. Scott Walker’s campaign illegally coordinated with conservative groups during his 2012 recall campaign. Writing for the court’s conservative majority in the 4-2 decision, Justice Michael Gableman minced no words. “To be clear,” Gableman wrote, “this conclusion ends the John Doe investigation.” ## Understanding Wisconsin, Together. WPR’s “Wisconsin Today” newsletter keeps you connected to the state you love without feeling overwhelmed. No paywall. No agenda. No [...]

3. **Leaked documents reveal secretive influence of corporate cash on politics | US political financing | The Guardian**
   URL: https://www.theguardian.com/us-news/2016/sep/14/corporate-cash-john-doe-files-scott-walker-wisconsin
   Content: Walker’s campaign told the Guardian that the John Doe investigation was “baseless” and had been shut down multiple times by the state courts. “There is absolutely no evidence of any wrongdoing,” a spokesman said. The third-party lobbying groups that were the subject of the investigation said the prosecutors had accused wholly innocent individuals of crimes that did not exist under state law. They insisted they had a right to comment about public officials and policy and to protect the confidentiality of their donors. ## Most viewed ## Most viewed [...] In 2015, Justice Prosser refused to recuse himself from a case in which the state supreme court sat in judgment over the John Doe [...]

4. **In Search of John Doe No. 2: The Story the Feds Never Told About ...**
   URL: https://www.motherjones.com/politics/2007/07/search-john-doe-no-2-story-feds-never-told-about-oklahoma-city-bombing/
   Content: After more than a year of proceedings, in August 1997, the grand jury (which, like all such panels, had heard only evidence selected by the government) concluded its investigation without issuing any criminal indictments. The doj held back the news for two months while staff in Washington met to devise a roll-out plan that a doj aide compared to “coordinating the invasion of Normandy.” The plan targeted the media as well as Senators Orrin Hatch (R-Utah) and Byron Dorgan (D-N.D.), who, thanks to Jesse Trentadue’s efforts, had taken an interest in the case. In a Senate Judiciary Committee hearing a few months earlier, Hatch had quizzed then-Attorney General Janet Reno about Kenney and [...]

5. **CMD Urges U.S. Supreme Court to Hear Prosecutors' Appeal in John Doe II Corruption Case - EXPOSEDbyCMD**
   URL: https://www.exposedbycmd.org/2016/06/23/cmd-urges-u-s-supreme-court-to-hear-prosecutors-appeal-in-john-doe-ii-corruption-case/
   Content: State Justices David Prosser and Michael Gableman denied a motion from the special prosecutor to step aside and then proceeded to help “cancel oral argument, issue sweeping secrecy orders, halt the investigation, fire the special prosecutor, order the evidence returned and copies destroyed, and dramatically curtail Wisconsin’s campaign finance law, rendering the longstanding limits and other restrictions the state places on contributions to candidates virtually meaningless.” They have even sought inappropriately to impede the prosecutors’ appeal to the U.S. Supreme Court. Specifically, the brief argues that: [...] Even more troubling, the special prosecutor may have unearthed documents [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 13. PolitiFact / pf_003 - true

#### Input
- **Claim:** Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources indicate Hatch co-sponsored a 1993 health bill containing an individual mandate.
- **Explanation:** PolitiFact directly states that Hatch was the co-sponsor of a 1993 Republican-backed bill that included an individual mandate (Source 1). Fox News and The New Yorker also say the individual mandate appeared in 1993 bills supported/co-sponsored by Orrin Hatch (Sources 2 and 3). None of the provided sources contradict the claim; they only discuss later opposition or related details.
- **Confidence reason:** Multiple sources support, but details of the exact bill are not fully corroborated.
- **Claim verdicts:**
```json
[
  {
    "claim": "Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/": "supporting",
  "https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long": "supporting",
  "https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate": "supporting",
  "https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf": "neutral",
  "https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Hatch once supported an individual mandate, said Cenk Uygur**
   URL: https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/
   Content: We contacted Hatch's office to ask for an explanation for Hatch's change of position, but we didn't hear back. Last year, Kaiser Health News interviewed former Sen. Dave Durenberger, R-Minn., who had also co-sponsored the plan. Durenberger said that it was Republicans who had changed in the years since 1993, backing away from policies on health care they once supported. Uygur asked, "Did you know that Hatch co-sponsored the 1993 bill that had an individual mandate?" We didn't, but we checked the record. Hatch was the co-sponsor of a Republican-backed bill that included an individual mandate. We rate Uygur's statement True. [...] "Here's what I'm amazed by -- Orrin Hatch," Uygur said. [...]

2. **Individual health care insurance mandate has roots two decades long | Fox News**
   URL: https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long
   Content: The mandate, requiring every American to purchase health insurance, appeared in a 1989 published proposal by Stuart M. Butler of the conservative Heritage Foundation called "Assuring Affordable Health Care for All Americans," which included a provision to "mandate all households to obtain adequate insurance." The Heritage Foundation "substantially revised" its proposal four years later, according to a 1994 analysis by the Congressional Budget Office. But the idea of an individual health insurance mandate later appeared in two bills introduced by Republican lawmakers in 1993, according to the non-partisan research group ProCon.org. Among the supporters of the bills were senators Orrin [...]

3. **Unpopular Mandate | The New Yorker**
   URL: https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate
   Content: In February, 2012, Stuart Butler, the author of the Heritage Foundation brief that first proposed the mandate, wrote an op-ed for USA Today in which he recanted that support. “I’ve altered my views on many things,” he wrote. “The individual mandate in health care is one of them.” Senator Orrin Hatch, who had been a co-sponsor of the Chafee bill, emerged as one of the mandate’s most implacable opponents in 2010, writing in The Hill that to come to “any other conclusion” than that the mandate is unconstitutional “requires treating the Constitution as the servant, rather than the master, of Congress.” Mitt Romney, who had both passed an individual mandate as governor and supported Wyden- [...]

4. **[PDF] The New Bipartisan Consensus for an Individual Mandate**
   URL: https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf
   Content: Affordability, Responsibility, and Empowerment Act (PCARE) introduced by Republican Senators Orrin Hatch and Richard Burr, together with Congressman Fred Upton, it is now clear HEALTH POLICY CENTER The New Bipartisan Consensus for an Individual Mandate that there is at least some bipartisan agreement on the need for an individual mandate for health insurance. Although the official description of the PCARE proposal includes language indicating strong objection to the individual responsibility requirement of the Affordable Care Act (ACA), the proposal uses different types of penalties intended to bring most Americans into the health insurance pool and keep them there.1 According to the [...]

5. **How Sen. Orrin Hatch Changed America's Health Care - KFF Health News**
   URL: https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/
   Content: Some legislators and consumer advocacy groups wanted vitamins and other supplements to go through a tight approval process, akin to the testing the Food and Drug Administration requires of drugs. But DSHEA reined in the FDA, determining that supplements do not have to meet the same safety and efficacy standards as prescription drugs. That legislative clamp on regulation has led to ongoing questions about whether dietary supplements actually work and concerns about how they interact with other medications patients may be taking. DSHEA was co-sponsored by Democrat Tom Harkin, then a senator from Iowa. [...] “AIDS does not play favorites,” Hatch told other senators. “It affects rich and [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 14. PolitiFact / pf_004 - barely-true

#### Input
- **Claim:** Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** None of the provided sources show Mark Herring voting on shorter sentences for sex offenders.
- **Explanation:** The sources provided do not mention Mark Herring or any vote by him on sentencing lengths for sex offenders, including rapists. Source 1 discusses sex-offender recidivism research generally, Source 2 provides broader information on sexual offending prevalence, Source 3 summarizes Canadian bail/sentencing reforms without linking to Mark Herring, and Sources 4–5 are unrelated to the specific voting claim.
- **Confidence reason:** No source addresses Mark Herring’s vote or the alleged sentencing change.
- **Claim verdicts:**
```json
[
  {
    "claim": "Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf": "neutral",
  "https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf": "neutral",
  "https://openparliament.ca/bills/45-1/C-14/?singlepage=1": "neutral",
  "https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf": "neutral",
  "https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf": "neutral"
}
```

#### Search Evidence Input
1. **[PDF] Recidivism: The Great Lie of “Frightening and High” - Regulations.gov**
   URL: https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf
   Content: First of all, specialization is no more common for sex offenders than any other type of offender; thieves are more likely to steal, drug offenders are more likely to commit drug crimes, et cetera. Furthermore, strong evidence suggests people convicted of sexual offenses actually specialize at a lower rate than most other offenses. The 2000 Michigan Parole Board study shows people convicted of sexual offenses committed subsequent sexual offenses (2.46%) at a lower rate than forgers committing forgery (6.86%), burglars committing burglary (10.56%), robbers committing robbery (5.17%), drug offenders committing drug crimes (6.42%), and larcenists committing larceny (12.65%). "Langan and [...]

2. **[PDF] Sex Offender Management Assessment and Planning Initiative**
   URL: https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf
   Content: colleagues (2007) conducted a national telephone survey of 5,000 women aged 18–86, including approximately 3,000 who represented all women in the United States and 2,000 women attending college. The research results indicated that for women of all ages, an estimated 18 percent had been raped during their lifetime. This translates into an estimated 20 million victims of rape out of 112 million women in the United States. In looking at past-year victimization alone, the authors estimated that more than 1 million women had been raped. Of those who reported that they were raped, 16 percent indicated they had reported the crime to law enforcement. The study found that victims of drug- [...]

3. **Bill C-14 | openparliament.ca**
   URL: https://openparliament.ca/bills/45-1/C-14/?singlepage=1
   Content: Crime is a real concern throughout the country. Canadians are frustrated to see repeat violent offenders being released from prison. They are concerned about their safety. We see it every day: Car thefts and break-ins in the middle of the night are being caught on camera. People simply want to know that the system puts their safety first. [...] ## Debate Summary line drawing of robot This is a computer-generated summary of the speeches below. Usually it’s accurate, but every now and then it’ll contain inaccuracies or total fabrications. Bill C-14 proposes reforms to Canada's bail and sentencing laws, including changes to reverse onus provisions, bail conditions, sentencing factors, and [...]

4. **[PDF] DISSENTING REPORT - Supreme Court of Ohio**
   URL: https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf
   Content: by the police officer and the windfall afforded a guilty defendant by application of the rule is contrary to the idea of proportionality that is essential to the concept of justice.” It is well known that “[t]he principal cost of applying any exclusionary rule ‘is, of course, letting guilty and possibly dangerous criminals go free .’” Montejo v. Louisiana, 129 S.Ct. 2079, 2090 (2009) (quoting Herring v. United States, 555 U.S. 135, 141 (2009)). Letting the guilty go free is “something that ‘offends basic concepts of the criminal justice system.’” Herring, 129 S.Ct. at 701, quoting Leon, 468 U.S. at 908. “‘[T]he rule’s costly toll upon truth-seeking and law enforcement objectives [...]

5. **[PDF] Recommendations for SSOSA reforms; treatment alternatives for ...**
   URL: https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf
   Content: internet would be different from cases where someone was actually interacting with a child via the internet”. He further stated “this offense in part resembles 25 McWhorter, S., Stander, V., Merrill, L., Thomsen, S., & Milner, J. (200=9). Reports of rape reperpetration by newly enlisted male navy personnel. Violence and Victims, 24 (2), 209-224. doi: 10.1891/0886-6708.24.2.204 26 Dietz (2020). Denial and minimization among sex offenders. Behavior Sciences & the Law, 38, 571-585. doi: 10.1002/bsl.2493 27 Hernandez (2000). Self-reported contact sexual offenses by participants in the Federal Bureau of Prisons’ Sex Offender Treatment Program: Implications for internet sex offenses. Bureau [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 15. PolitiFact / pf_009 - true

#### Input
- **Claim:** The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true`
- **TLDR:** Sources show the slur was used, but none link it to Nazi genocide justification.
- **Explanation:** Source 1 confirms Ted Nugent used the phrase “subhuman mongrel” for President Obama, but it does not connect the phrase to Nazi rhetoric or genocide justification. Source 3 describes Nazi dehumanization and genocide in general (via the Nuremberg Laws and subsequent “Final Solution”), but it does not mention this specific phrase or claim that Nazis used it to justify genocide of Jews.
- **Confidence reason:** Slur usage is documented; Nazi-phrase/genocide link is absent.
- **Claim verdicts:**
```json
[
  {
    "claim": "The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.csmonitor.com/USA/Politics/Decoder/2014/0221/Ted-Nugent-apologizes-to-President-Obama.-Sincere": "supporting",
  "https://everytownresearch.org/report/extreme-right/": "neutral",
  "https://www.nationalww2museum.org/war/articles/nuremberg-laws": "neutral",
  "https://en.wikipedia.org/wiki/Holocaust_denial": "neutral",
  "https://www.adl.org/resources/backgrounder/debunking-holocaust-denial-claims": "neutral"
}
```

#### Search Evidence Input
1. **Ted Nugent apologizes to President Obama. Sincere? - CSMonitor.com**
   URL: https://www.csmonitor.com/USA/Politics/Decoder/2014/0221/Ted-Nugent-apologizes-to-President-Obama.-Sincere
   Content: By Peter Grier Staff writer @petergrier Ted Nugent has apologized for calling President Obama a “subhuman mongrel.” The shock rocker/political provocateur on Friday told conservative radio host and CNN commentator Ben Ferguson that he “did cross the line” with those words, uttered in an interview with Guns.com in January. At first Nugent did not apologize directly to Mr. Obama himself. Instead, his main regret seemed to be that the controversy over his unrestrained rhetoric was affecting the man he campaigned with in Texas this week, state Attorney General and presumptive GOP gubernatorial candidate Greg Abbott, as well as other top GOP figures such as Sen. Ted Cruz of Texas. [...] # [...]

2. **Armed and Dangerous: How the Gun Lobby Enshrines Guns as Tools of the Extreme Right | Everytown Research & Policy**
   URL: https://everytownresearch.org/report/extreme-right/
   Content: and Peter Finn, “Prospect of Ban Drives a Surge in Demand for Assault Weapons,” Washington Post, January 17, 2013, . NRA leaders also deployed racist rhetoric to denigrate President Obama, with one board member calling him a “subhuman mongrel” and LaPierre declaring that “eight years of one demographically-symbolic president is enough.”77)“Ted Nugent: Obama a ‘Subhuman Mongrel,’” Politico, February 21, 2014, ; Alexandra Jaffe, “NRA’s Wayne LaPierre: Obama, Clinton ‘Demographically-Symbolic,’” CNN, April 15, 2015, .

3. **The Nuremberg Race Laws | The National WWII Museum | New Orleans**
   URL: https://www.nationalww2museum.org/war/articles/nuremberg-laws
   Content: subjects” without rights creates the preconditions to justify dehumanization, deportation, and genocide—a process that began in earnest with the passage of the Nuremberg Laws. [...] landscape encouraged darker “solutions” to the “Jewish problem,” resulting in the mass murder by shooting of over 1.5 million Jews on the Eastern Front. From there, Nazi leaders decided to deport the millions trapped in ghettos to static death camps where they were gassed en masse. This so-called “Final Solution” saw 1.8 million Jews murdered at Bełżec, Sobibór, and Treblinka, and another 1.1 million murdered at Auschwitz. [...] Historian Thomas Childers writes, “it was also symptomatic of Hitler’s modus [...]

4. **Holocaust denial - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Holocaust_denial
   Content: Holocaust denial is the negationist and antisemitic claim that Nazi Germany and its collaborators did not commit genocide against European Jews during World War II, ignoring overwhelming historical evidence to the contrary. Theories assert that the genocide of Jews is a fabrication or exaggeration. Holocaust denial includes making one or more of the following false claims: that Nazi Germany's "Final Solution" was aimed only at deporting Jews from the territory of the Third Reich and did not include their extermination; that Nazi authorities did not use extermination camps and gas chambers for the mass murder of Jews; that the actual number of Jews murdered is significantly lower than [...]

5. **Debunking Holocaust Denial Claims | ADL**
   URL: https://www.adl.org/resources/backgrounder/debunking-holocaust-denial-claims
   Content: Deniers Debunked The lack of a “master document” does not mean that the genocide of European Jews did not occur. The “Final Solution” — the Nazis’ comprehensive plan to murder all European Jews — was, as the Encyclopedia of the Holocaust observes, “the culmination of a long evolution of Nazi Jewish policy.” The destruction process was shaped gradually: it consisted of many thousands of directives, some written and some verbal. [...] Subsequent testimony by the architects of the Holocaust corroborates this fact pattern. Eichmann, while awaiting trial in Israel in 1960, related that Heydrich had told him in August 1941 that “the Führer has ordered the physical extermination of the Jews.” [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 16. PolitiFact / pf_011 - true

#### Input
- **Claim:** Says Donald Trump has changed his mind on abortion.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** The sources support that Trump shifted away from a national abortion ban toward state control.
- **Explanation:** FactCheck.org reports that during the 2024 campaign Trump said he would not sign a national abortion ban, describing it as a change from his 2016 position supporting a federal abortion ban after 20 weeks (Source 1) and noting he left abortion to states (Source 3). Al Jazeera similarly quotes Trump saying states determine abortion policy by vote or legislation (Source 4). The sources do not directly address every nuance of “changed his mind,” but they do support a shift in stated approach.
- **Confidence reason:** Multiple sources directly describe a shift to state control.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Donald Trump has changed his mind on abortion.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/": "supporting",
  "https://www.factcheck.org/2023/09/trump-walked-back-abortion-statement-misleadingly-used-in-biden-harris-ad/": "neutral",
  "https://www.factcheck.org/2024/05/biden-twists-trumps-comments-on-tracking-pregnancies-and-punishing-women-who-get-abortions/": "supporting",
  "https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed": "supporting",
  "https://www.aclu.org/trump-on-abortion": "neutral"
}
```

#### Search Evidence Input
1. **Trump's 'Like It or Not' Comment and Harris' Response - FactCheck.org**
   URL: https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/
   Content: Of course, we don’t know what Trump will do in the future, but as we’ve written, Trump during this campaign has said he won’t sign a national abortion ban, a change from his position in 2016, when Trump backed a federal abortion ban after 20 weeks of pregnancy. He says he’s against restrictions on birth control, and he supports IVF, or in vitro fertilization. Trump has said it’s up to states to decide if they want to monitor women’s pregnancies. [...] Harris also cited Project 2025. “And we know that what he has planned includes a national abortion ban, restricting access to birth control, putting IVF treatments at risk, and forcing states to monitor women’s pregnancies. You don’t have [...]

2. **Trump Walked Back Abortion Statement Misleadingly Used in Biden-Harris Ad - FactCheck.org**
   URL: https://www.factcheck.org/2023/09/trump-walked-back-abortion-statement-misleadingly-used-in-biden-harris-ad/
   Content: But the ad leaves out what Trump said later that evening, after his comments were roundly criticized by groups both for and against abortion rights. In a statement published on his website, Trump took back his town hall answer. > Trump statement, March 30, 2016: If Congress were to pass legislation making abortion illegal and the federal courts upheld this legislation, or any state were permitted to ban abortion under state and federal law, the doctor or any other person performing this illegal act upon a woman would be held legally responsible, not the woman. The woman is a victim in this case as is the life in her womb. My position has not changed — like Ronald Reagan, I am pro-life [...]

3. **Biden Twists Trump's Comments on Tracking Pregnancies and Punishing Women Who Get Abortions - FactCheck.org**
   URL: https://www.factcheck.org/2024/05/biden-twists-trumps-comments-on-tracking-pregnancies-and-punishing-women-who-get-abortions/
   Content: Other Democrats echoed Biden’s claim. For example, Michigan Gov. Gretchen Whitmer claimed Trump “said again that women should be punished for having abortions. And he’s okay with states monitoring pregnant women to stop them from having abortions.” New York Gov. Kathy Hochul cited Trump’s Time interview as evidence that he “endorses punishing women who get an abortion.” But again, those were not Trump’s words, and the Democrats’ claims twist his message. [...] In several campaign speeches, however, President Joe Biden has twisted Trump’s words, claiming that Trump said “states should monitor women’s pregnancies and prosecute those who violate abortion bans.” (Emphasis is ours.) In the [...]

4. **‘Let states decide’: How Donald Trump’s position on abortion has changed | Donald Trump News | Al Jazeera**
   URL: https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed
   Content: In a video posted on his social media platform, Truth Social, Trump said: “My view is now that we have abortion where everybody wanted it from a legal standpoint, the states will determine by vote or legislation or perhaps both. And whatever they decide must be the law of the land – in this case, the law of the state.” ## Recommended Stories He also took credit for the overturning of Roe v Wade by the US Supreme Court in 2022, a decision that led to 24 US states enacting laws banning nearly all abortions by January 2023. On the other hand, he voiced his support for abortion under three exceptions, in cases of rape, incest and when the life of the mother is at risk. Until now, Trump’s [...]

5. **Trump on Abortion | American Civil Liberties Union**
   URL: https://www.aclu.org/trump-on-abortion
   Content: The threats to people’s ability to control their bodies and their reproductive lives don’t stop with attempts to outlaw abortion. For example, Trump recently admitted that he was looking at ways to restrict access to contraception. While electoral realities forced him to attempt to walk back that statement, as one of the leading anti-reproductive-health members of Trump’s administration recently explained, Trump’s “track record is the best evidence, I think, you could have of what a second term might look like if Trump wins.” That track record includes, among other things, changing federal rules that decimated access to birth control for low-income people by forcing Planned Parenthood [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 17. PolitiFact / pf_014 - half-true

#### Input
- **Claim:** Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources don’t provide the claimed survey result or the “amnesty” motivation figure.
- **Explanation:** None of the provided sources include a survey stating that 95% of people caught crossing the U.S.-Mexico border said they were coming because they were promised amnesty. Source 1 discusses border apprehension declines and mentions “amnesty plan” rhetoric, but it does not present the specific survey statistic or the claimed motivation breakdown. Source 2 and Source 3 discuss broader immigration/asylum context and “word has gotten out” claims, but they do not provide the exact “95 percent” survey finding.
- **Confidence reason:** No source contains the specific survey statistic or wording.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://cis.org/Arthur/Fact-Check-Illegal-Immigration-Down-90-Percent-Thanks-Biden": "neutral",
  "https://cis.org/Arthur/Who-FactChecks-FactCheckers": "neutral",
  "https://www.npr.org/2018/11/27/670807343/fact-check-whats-happening-on-the-u-s-mexico-border": "neutral",
  "https://azcir.org/news/2025/03/03/did-encounters-us-mexico-border-drop-by-95percent-in-first-week-of-trump-presidency-no/": "neutral",
  "https://www.congress.gov/event/113th-congress/house-event/LC29861/text": "neutral"
}
```

#### Search Evidence Input
1. **Fact Check: Illegal Immigration Down ‘90 Percent’ Thanks to Biden**
   URL: https://cis.org/Arthur/Fact-Check-Illegal-Immigration-Down-90-Percent-Thanks-Biden
   Content: In March, agents at the U.S.-Mexico line apprehended 3,811 nationals of those four countries, which is a 95 percent decline from December, when apprehensions of aliens from those countries totaled more than 84,000 — the highest figure for those four nationalities, again, ever. But the March figure was still a 235 percent increase over Southwest border apprehensions for nationals of those four countries in March 2020 (admittedly the month that the Covid-19 pandemic was declared), and a higher apprehension total than in any month when Joe Biden wasn’t president, in whole or part (4,410 Venezuelans, Nicaraguans, Haitians, and Cubans were caught entering illegally in January 2021). With a [...]

2. **Who Fact-Checks the Fact-Checkers?**
   URL: https://cis.org/Arthur/Who-FactChecks-FactCheckers
   Content: By contrast, according to CBP statistics, in FY 2019 CBP is now averaging 31,188 family units and UACs detained at and between the ports of entry a month, a 136 percent increase over FY 2017. In December 2018, in fact, almost 61 percent of all aliens deemed inadmissible at the ports of entry and apprehended entering between the ports were family units or UACs. Of those family units apprehended between the ports of entry, 95 percent are from El Salvador, Guatemala, or Honduras. Under the Flores settlement agreement and the 2008 Trafficking Victims Protection Reauthorization Act (TVPRA), the children in those family units must be released in 20 days, as I explained in my May 2018 [...]

3. **FACT CHECK: What's Happening On The U.S.-Mexico Border? : NPR**
   URL: https://www.npr.org/2018/11/27/670807343/fact-check-whats-happening-on-the-u-s-mexico-border
   Content: What is asylum? Seeking asylum means asking the U.S. to accept you — legally — because of persecution you are facing in your home country. Crossing the border illegally is a misdemeanor; for a person who has already been deported once, it's a felony. Seeking asylum at a port of entry, however, is not a crime at all. However, authorities at legal border crossings have been limiting the number of people who can request asylum. Only 40 to 100 people are allowed each day, Fredrick says. "People in the caravan who want to request asylum, they're looking at months to even be heard first by U.S. authorities, and then for that claim to be processed can take months or even years," Fredrick [...]

4. **FACT BRIEF: Did encounters at the U.S.-Mexico border decrease by 95% in the first week of Trump’s presidency?**
   URL: https://azcir.org/news/2025/03/03/did-encounters-us-mexico-border-drop-by-95percent-in-first-week-of-trump-presidency-no/
   Content: The Arizona Center for Investigative Reporting partners with Gigafact to produce fact briefs, or quick-response fact checks, about trending claims relating to Arizona. ## Sources Support AZCIR with a donation! Your support makes our work possible! Sign Up, Stay Informed The Arizona Center for Investigative Reporting is partnering with Gigafact to produce timely fact briefs, or quick-response fact checks, about trending claims relating to Arizona. gigafact logo for fact briefs azcir logo for fact briefs ### RELATED Avatar photo ## Carmela GuaglianoneAZCIR Fact Checker Carmela Guaglianone is a fact-checker for the Arizona Center for Investigative Reporting, working in partnership with [...]

5. **OPEN BORDERS: THE IMPACT OF PRESIDENTIAL AMNESTY ON BORDER SECURITY | Congress.gov | Library of Congress**
   URL: https://www.congress.gov/event/113th-congress/house-event/LC29861/text
   Content: Mexico and Central America, we are simply fooling ourselves. We will see a wave of illegal immigration because of the President's actions. At its core, the President's unilateral amnesty plan is deeply unfair to the millions who are waiting in line to become a part of our great Nation, and it demonstrates reckless disregard for America's security. We have a formal immigration process for a reason: To promote fairness in allowing people to enter the United States and to keep those who will seek to do us harm outside of our borders. Sadly, the Department of Homeland Security is unprepared to handle the coming surge that the President's policies will incite. The Border Patrol's resources [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 18. PolitiFact / pf_017 - true

#### Input
- **Claim:** In the last 10 years, Georgias middle class income has dropped $6,500.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mixed`, expected one of `true`
- **TLDR:** Sources partially support a ~$6,500 middle-class income drop, but not clearly for the last 10 years.
- **Explanation:** Source 2 (PolitiFact) explicitly discusses a claim that middle-class income dropped $6,500 in 10 years and says it matches Census Bureau data, citing a $6,682 drop (inflation-adjusted) from 2002 to 2012. Source 1 (GBPI) supports broader income declines (e.g., median household income fell nearly $8,000 from 2007 to 2011 and middle-class Georgians bring home ~7% less income as of 2016 than in 2000), but it does not directly quantify a $6,500 drop over the last 10 years. Source 3 and Source 5 provide median household income levels but do not address the specific “middle class” and “last 10 years” $6,500 figure.
- **Confidence reason:** One source directly addresses the $6,500/10-year figure; others are indirect.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the last 10 years, Georgias middle class income has dropped $6,500.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.gbpi.org/wp-content/uploads/2018/02/Georgias-People-Hold-Untapped-Value.pdf": "supporting",
  "https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/": "supporting",
  "https://www.neilsberg.com/insights/georgia-median-household-income/": "neutral",
  "https://www.incomebyzipcode.com/georgia": "neutral",
  "https://www.census.gov/quickfacts/fact/table/GA/INC110224": "neutral"
}
```

#### Search Evidence Input
1. **Fact Sheet: Georgians Hold Untapped Potential**
   URL: https://www.gbpi.org/wp-content/uploads/2018/02/Georgias-People-Hold-Untapped-Value.pdf
   Content: brought home about as much in annual income as families in other states. But their earnings slipped soon after the millennium and crashed during the Great Recession. Georgia’s median household income fell by nearly $8,000 from 2007 to 2011, steeper than the nation as a whole. As of 2016, middle class Georgians bring home about 7 percent less income than in 2000. Economic struggle limits families’ ability to thrive, especially for groups historically excluded from opportunity. About 23 percent of children in Georgia, 14 percent of working-age adults and 10 percent of seniors in 2016 struggled to get by, as measured by people who live below the federal poverty line. That’s less than [...]

2. **PolitiFact | Carter claim about median household income on target**
   URL: https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/
   Content: "What we saw with the Great Recession, starting around 2007, was employment and income just really fell through the floor due to the collapse of the housing market, the collapse of the stock market," Tharpe said. "Those really hurt Georgia because of our reliance on the housing industry and construction jobs." Since that crash, the economy has been gradually moving in the right direction, he said. "But incomes and the ability for families to make a living and make ends meet is really lagging behind," Tharpe said. "We haven’t really seen that much growth since we hit that floor." In summary, Carter’s ad says middle-class income has dropped $6,500 in 10 years. [...] Nationally, in that [...]

3. **Georgia Median Household Income - 2025 Update | Neilsberg**
   URL: https://www.neilsberg.com/insights/georgia-median-household-income/
   Content: | Year | Median Household Income | YOY Change($) | YOY Change(%) | --- --- | | 2010 | 69,330 - | | 2011 | 67,716 | -1,614 | -2.33% | | 2012 | 66,153 | -1,563 | -2.31% | | 2013 | 64,609 | -1,544 | -2.33% | | 2014 | 63,760 | -849 | -1.31% | | 2015 | 64,009 | 249 | 0.39% | | 2016 | 64,997 | 988 | 1.54% | | 2017 | 66,063 | 1,066 | 1.64% | | 2018 | 67,777 | 1,714 | 2.59% | | 2019 | 70,181 | 2,404 | 3.55% | | 2020 | 72,237 | 2,056 | 2.93% | | 2021 | 73,191 | 954 | 1.32% | | 2022 | 74,298 | 1,107 | 1.51% | | 2023 | 74,664 | 366 | 0.49% | TABLE OF CONTENTS Georgia median household income trends: 2000 to 2023 Median household income in Georgia by household size Georgia income distribution and [...]

4. **Georgia Income Statistics | Current Census Data for Georgia Zip Codes**
   URL: https://www.incomebyzipcode.com/georgia
   Content: ### Georgia Income Levels or Income Distribution | | | | --- | Households | 4,074,366 | 100% | | Less than $10,000 | 219,526 | 5% | | $10,000 to $14,999 | 138,699 | 3% | | $15,000 to $19,999 | 128,174 | 3% | | $20,000 to $24,999 | 139,522 | 3% | | $25,000 to $29,999 | 135,539 | 3% | | $30,000 to $34,999 | 141,222 | 3% | | $35,000 to $39,999 | 146,930 | 4% | | $40,000 to $44,999 | 146,243 | 4% | | $45,000 to $49,999 | 141,769 | 3% | | $50,000 to $59,999 | 265,754 | 7% | | $60,000 to $74,999 | 380,471 | 9% | | $75,000 to $99,999 | 529,016 | 13% | | $100,000 to $124,999 | 411,252 | 10% | | $125,000 to $149,999 | 293,369 | 7% | | $150,000 to $199,999 | 373,457 | 9% | | $200,000 or more | [...]

5. **U.S. Census Bureau QuickFacts: Georgia**
   URL: https://www.census.gov/quickfacts/fact/table/GA/INC110224
   Content: | Total health care and social assistance receipts/revenue, 2022 ($1,000)(c) | 95,053,842 | | Total transportation and warehousing receipts/revenue, 2022 ($1,000)(c) | 55,684,552 | | Total retail sales, 2022 ($1,000)(c) | 216,836,912 | | Total retail sales per capita, 2022(c) | $19,869 | | Transportation | | --- | | Mean travel time to work (minutes), workers age 16 years+, 2020-2024 | 28.3 | | Income & Poverty | | --- | | Median households income (in 2024 dollars), 2020-2024 | $77,353 | | Per capita income in past 12 months (in 2024 dollars), 2020-2024 | $40,924 | | Persons in poverty, percent |  12.6% | [...] ### Table | All Topics Population Age and Sex Race and Hispanic Origin [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 19. PolitiFact / pf_018 - half-true

#### Input
- **Claim:** Oil production is down 14 percent this year on federal land.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources discuss overall U.S. crude forecasts, not a 14% federal-land drop.
- **Explanation:** None of the provided sources state that oil production on federal land is down 14% this year. Source 5 (EIA) forecasts total U.S. crude production averaging 13.5 million b/d in 2026, about 100,000 b/d less than 2025, and Source 1 discusses EIA STEO projections for 2026/2027, including Federal Gulf of America levels—but neither provides a “down 14 percent this year on federal land” figure. Source 3 and Source 4 also only describe modest declines in overall U.S. crude production, without the specific federal-land and 14% claim.
- **Confidence reason:** No source provides the specific 14% federal-land figure.
- **Claim verdicts:**
```json
[
  {
    "claim": "Oil production is down 14 percent this year on federal land.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/": "neutral",
  "https://www.factcheck.org/issue/oil-production/": "neutral",
  "https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/": "neutral",
  "https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/": "neutral",
  "https://www.eia.gov/todayinenergy/detail.php?id=66844": "neutral"
}
```

#### Search Evidence Input
1. **EIA Sees USA Crude Oil Production Dropping in 2026, 2027 | Rigzone**
   URL: https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/
   Content: In 2025, Lower 48 States production averaged 11.28 million barrels per day, Federal Gulf of America production came in at 1.91 million barrels per day, and Alaska output averaged 0.42 million barrels per day, the STEO showed. A quarterly breakdown included in the EIA’s latest STEO projected that U.S. crude oil production will come in at 13.73 million barrels per day in the first quarter of this year, 13.65 million barrels per day in the second quarter, 13.47 million barrels per day in the third quarter, 13.50 million barrels per day in the fourth quarter, 13.43 million barrels per day in the first quarter of 2027, 13.31 million barrels per day in the second quarter, and 13.13 million [...]

2. **oil production Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/oil-production/
   Content: FactCheck.org® A Project of The Annenberg Public Policy Center Become a Facebook fan Follow us on Twitter Get the RSS feed Follow on Insta Sign up for the email newsletter Help us hold politicians accountable. # Issues: oil production ### FactChecking Trump’s State of the Union Address FactChecking Trump’s State of the Union Address February 25, 2026 In the first State of the Union address of his second term, President Donald Trump proclaimed that “our nation is back, bigger, better, richer and stronger than ever before.” But our review of his speech found that he distorted a number of facts about the state of the economy, health care, immigration and other topics. ### Trump’s Numbers, [...]

3. **EIA sees 2026 oil production decline despite regional growth EIA sees 2026 oil production decline despite regional growth**
   URL: https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/
   Content: This marginal dip marks a turning point after steady expansion in US oil output driven primarily by shale plays and offshore developments. The EIA attributes the projected decline to a combination of weaker growth in key producing regions and lower oil prices, which may disincentivize new drilling. Production growth in 2025 was largely concentrated in the Permian Basin, with additional contributions from federal offshore areas in the Gulf of Mexico and new developments in Alaska. However, those gains are expected to taper or be outpaced by declines in other mature or cost-constrained regions across the Lower 48 states. Even with ongoing efficiencies, the pace of well completions is [...]

4. **U.S. energy agency forecasts a modest dip in domestic crude production in 2026**
   URL: https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/
   Content: March 24, 2026 BLM formal protest ### BLM initiates formal protest window ahead of Utah oil and gas lease auction scheduled for March 31, 2026 March 23, 2026 BLM lease, oil and gas rig ### BLM launches early stakeholder feedback process for August 2026 oil and gas lease auction in Montana and North Dakota March 22, 2026 The EIA has reported that US crude oil production will average approximately 13.5 million barrels per day (b/d) this year, which is roughly 100,000 b/d less than in 2025. The forecast follows four years of substantial crude oil production growth in the United States. ### The Permian Basin: A cornerstone of the United States oil and gas industries [...] Gastech The [...]

5. **EIA forecasts U.S. crude oil production will decrease slightly in 2026 - U.S. Energy Information Administration (EIA)**
   URL: https://www.eia.gov/todayinenergy/detail.php?id=66844
   Content: In our latest Short-Term Energy Outlook, we forecast U.S. crude oil production will average 13.5 million barrels per day (b/d) in 2026, about 100,000 b/d less than in 2025. This forecast decline in production follows four years of rising crude oil output. Production increased by 0.3 million b/d in 2024 and by 0.4 million b/d in 2025, mostly because of increased output in the Permian Basin in Texas and New Mexico. In 2026, we forecast modest production increases in Alaska, the Federal Gulf of America, and the Permian will be offset by declines in other parts of the United States. We forecast that the West Texas Intermediate crude oil price will average $65 per barrel (b) in 2025 and [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 20. PolitiFact / pf_020 - pants-fire

#### Input
- **Claim:** U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence."
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `true`
- **Score:** `95`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `true`, expected one of `false`
- **TLDR:** PolitiFact directly reports Langevin opposed a border fence over fears someone would be hurt.
- **Explanation:** Source 1 (PolitiFact) explicitly states the claim: Langevin opposed a U.S.-Mexican border fence because he was afraid someone would get hurt trying to go around it. None of the other provided sources address Langevin’s stated reasons for opposing the fence.
- **Confidence reason:** Only one source directly addresses the specific rationale.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration \"because he is afraid that someone will get hurt trying to go around the fence.\"",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/": "supporting",
  "https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm": "neutral",
  "https://www.congress.gov/event/110th-congress/house-event/LC8330/text": "neutral",
  "https://docs.house.gov/meetings/FA/FA00/20210930/114085/HMKP-117-FA00-20210930-SD002.pdf": "neutral",
  "https://www.dhs.gov/sites/default/files/publications/dhs-congressional-logs-2011_0.pdf": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Gardiner says Langevin opposed U.S.-Mexican border fence for fear someone will get hurt**
   URL: https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/
   Content: U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence.". # Gardiner says Langevin opposed U.S.-Mexican border fence for fear someone will get hurt. Gardiner, one of three Republicans hoping to unseat Democratic U.S. Rep. James Langevin in the 2nd District, devotes a lot of space to the issue on a web page called Illegal Immigration: Costly and Unfair to Citizens, Tax payers, and Legal Residents. He sent us to a website called OnTheIssues.org, which tracks voting records on a variety of issues, and a web page called "James Langevin on Immigration.". So regardless of the real reason [...]

2. **CONSTRUCTION OPTIONS AND STRATEGIC PLACEMENT**
   URL: https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm
   Content: In fact, I have testified, as my good friend mentioned, on issues of border security and border enforcement many times before Members of Congress. Over 11

3. **HOMELAND SECURITY FAILURES: TWIC EXAMINED**
   URL: https://www.congress.gov/event/110th-congress/house-event/LC8330/text
   Content: - [x] Aging (Special) (95th-119th) - [x] Aging (Special) (95th-119th) - [x] Agriculture, Nutrition, and Forestry (95th-119th) - [x] Agriculture, Nutrition, and Forestry (95th-119th) - [x] Appropriations (93rd-119th) - [x] Appropriations (93rd-119th) - [x] Armed Services (93rd-119th) - [x] Armed Services (93rd-119th) - [x] Banking, Housing, and Urban Affairs (93rd-119th) - [x] Banking, Housing, and Urban Affairs (93rd-119th) - [x] Budget (94th-119th) - [x] Budget (94th-119th) - [x] Caucus on International Narcotics Control (99th-119th) - [x] Caucus on International Narcotics Control (99th-119th) - [x] Commerce, Science, and Transportation (95th-119th) - [x] Commerce, Science, and [...]

4. **[PDF] Sexual assaults rise as the Peace Corps fails its volunteers**
   URL: https://docs.house.gov/meetings/FA/FA00/20210930/114085/HMKP-117-FA00-20210930-SD002.pdf
   Content: Dyan Mazurana, a Tufts University professor who has studied sexual violence in the international aid community, said the Peace Corps’ sexual assault statistics depict “an organization that can’t get its act together.” She said the agency should shut down programs if Peace Corps staff can’t ensure its volunteers will be safe. Fucci is one of six former Peace Corps volunteers interviewed by USA TODAY who said they were sexually assaulted by people they lived or worked with. Murray, who left the agency later that year, recently reviewed USA TODAY’s analysis of the most recent five years of Peace Corps crime data and said the data on rape and aggravated sexual assault still suggests [...]

5. **[PDF] WP# Receive Date Congressman Name Subject of Request 892621 ...**
   URL: https://www.dhs.gov/sites/default/files/publications/dhs-congressional-logs-2011_0.pdf
   Content: 893738 l/24/2011 Congressman Lloyd Doggett status of an 1-601 waiver 893739 1/24/2011 Congressman Michael Doyle Customer is requesting theat the I-90 application be expedited 892069 113/2011 Senator Richard J. 893612 l/21/201 1 Senator Tom Harkin Status of an I-290B 892575 1/10/2011 Congressman Doc Hastings Customer is requesting the status of an 1-130 petition for her husband. Dingell address a problem with a constituent 893779 1/24/2011 Congressman Kevin McCarthy Customer is requesting assistance with obtaining his certificate of citizenship 892380 1/6/2011 Senator Claire McCask.ilJ Re the status o~(bW 3 J jr-730 cases. 892584 1/10/2011 Senator Claire McCaskill Requests the status of [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 21. PolitiFact / pf_022 - mostly-true

#### Input
- **Claim:** Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `mostly_true, true`
- **TLDR:** Sources confirm the layoffs and tax breaks, but the CEO-to-Kasich super PAC link is only partially supported.
- **Explanation:** PolitiFact (Source 1) repeats the ad’s allegation that Worthington received state tax breaks and later laid off 100 Ohioans, and it also states that an Associated Press investigation found JobsOhio recommended $619,000 in incentives for Worthington subsidiaries. However, the provided excerpts do not substantiate the specific detail that the company CEO cut a half-million-dollar check to Kasich’s super PAC; that part is only mentioned as an allegation in the ad text, not verified in the excerpt.
- **Confidence reason:** Layoffs and incentives are supported; CEO donation detail not verified here.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/": "supporting",
  "https://www.urban.org/2016-analysis/kasich-cut-income-taxes-ohio-raised-sales-taxes": "neutral",
  "https://www.dispatch.com/story/news/politics/state/2026/03/19/osu-ted-carter-scandal-involved-jobsohio-podcast-spending-transparency/89120669007/": "neutral",
  "https://ohiocapitaljournal.com/2026/04/17/ohio-republican-bill-slammed-as-another-tax-giveaway-for-the-rich/": "neutral",
  "https://taxpolicycenter.org/taxvox/ohio-lawmakers-turn-surprise-surplus-huge-tax-cut": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Ted Cruz ad revisits a controversy from Kasich’s governorship of Ohio**
   URL: https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/
   Content: "Right before John Kasich was governor, he collected $611,000 from a Fortune 500 corporation," the ad says. "After Kasich became governor, that same company received $619 grand in state tax breaks for job creation. But last year, the company laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasich’s super PAC. John Kasich, not for us." To find out whether it’s fact or fiction, let’s take each allegation one at a time. Kasich took money from a Fortune 500 company [...] Last year, the company laid off 100 Ohioans In March 2015, Worthington announced it was cutting 555 jobs nationwide, which included 115 in Ohio. The company blamed the loss of these jobs [...]

2. **Kasich cut income taxes in Ohio but raised sales taxes | Urban Institute**
   URL: https://www.urban.org/2016-analysis/kasich-cut-income-taxes-ohio-raised-sales-taxes
   Content: Skip to main content The Urban.org Logo - Research and Evidence - What We Do - Events - About - Connect Urban is a trusted source for changemakers seeking to create a world where everyone has the opportunity and power to thrive. Learn more about us. - About Urban - Mission and Values - Our Story - Collaborate With Us - Our People - Careers - Support Urban - Organizational Principles - For the Media - Contact Us Urban values sharing our insights widely and connecting with partners across the country. Learn how you can stay informed and support us. - Collaborate With Us - Subscribe for Email Updates - Support Urban's Work - Attend an Event - Explore Careers - Get Involved - For the Media [...]

3. **OSU Ted Carter scandal puts spotlight on JobsOhio spending**
   URL: https://www.dispatch.com/story/news/politics/state/2026/03/19/osu-ted-carter-scandal-involved-jobsohio-podcast-spending-transparency/89120669007/
   Content: JobsOhio is a private nonprofit funded by the state's liquor profits. Former Gov. John Kasich created the organization in 2011 to help Ohio attract new businesses and development without the bureaucracy of government. But Kasich said he was disappointed by JobsOhio's decision to sponsor a podcast that struck him as a "misguided and weak attempt to deal with workforce issues." "What concerns me most is the possibility of mission drift," Kasich said in a Facebook post. "JobsOhio was created for one purpose and one purpose only: to create jobs for Ohio. I fully understand the importance of building a strong workforce, but this was clearly a failed attempt." Ohio Attorney General Dave [...]

4. **Ohio Republican bill slammed as another tax giveaway for the rich • Ohio Capital Journal**
   URL: https://ohiocapitaljournal.com/2026/04/17/ohio-republican-bill-slammed-as-another-tax-giveaway-for-the-rich/
   Content: The 2013 LLC tax break, which provides 40% of its benefits to the largest 7% of limited liability businesses and costs taxpayers about $1 billion a year. JobsOhio was created in 2011 under Kasich’s leadership. It has given more than $1 billion in what used to be public money to business interests, but it has struggled to show that it’s created a significant number of jobs. It did, however, give $60,000 to a woman with whom former Ohio State President Ted Carter had an “inappropriate relationship” to make four podcasts. She only made one. The “flat” state income tax passed in 2025. Policy Matters said it will cost $1 billion a year, with 40% of the benefit flowing to people making over [...]

5. **Ohio Lawmakers Turn A Surprise Surplus Into A Huge Tax Cut | Tax Policy Center**
   URL: https://taxpolicycenter.org/taxvox/ohio-lawmakers-turn-surprise-surplus-huge-tax-cut
   Content: without any of Kasich’s proposed offsets. According to the official numbers, it would reduce revenues by about $500 million in 2015 and $100 million after that. Among the legislature’s changes: [...] double the state earned income tax credit (EITC). At the same time, it would increase an already-generous business tax deduction. In February, Republican Kasich—who was something of a deficit hawk during his years in Congress--presented a revised budget that would reduce tax collections by about $100 million in 2015 and 2016. Kasich would have expanded previously-enacted income tax cuts for businesses and individuals. But because he proposed to partially offset them with a higher [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 22. PolitiFact / pf_025 - mostly-true

#### Input
- **Claim:** Federal spending on entitlements is projected to consume all revenue by 2045.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `20`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `mostly_true, true`
- **TLDR:** CBO-based analysis in the sources says entitlements would not consume all federal revenue by 2045.
- **Explanation:** Source 1 directly evaluates the specific claim and concludes that using CBO’s current-law projections, entitlements would not consume every revenue dollar by 2045 (though they would take a larger share). Source 2 discusses entitlement spending rising and crowding out other spending, but it does not state that entitlements consume all revenue by 2045. Therefore, the provided sources mostly contradict the claim as stated.
- **Confidence reason:** Only one source directly addresses the 2045 “all revenue” wording.
- **Claim verdicts:**
```json
[
  {
    "claim": "Federal spending on entitlements is projected to consume all revenue by 2045.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/": "contradicting",
  "https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html": "neutral",
  "https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf": "neutral",
  "https://www.crfb.org/papers/explaining-federal-spending-and-revenue": "neutral",
  "https://budgetmodel.wharton.upenn.edu/t/Entitlements/": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Ohio Treasurer Josh Mandel says entitlement spending expected to consume all federal revenue by 2045**
   URL: https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/
   Content: The alternative projections were based on a realistic understanding of politics and policy -- and one such understanding was that Congress was almost certain to extend many if not all tax cuts. With a few exceptions, notably higher rates on families earning more than $450,000, that is close to what happened. So what did the alternative projections show about revenues and entitlements in 2045 -- that is, about Mandel’s claim? [...] Mandel’s debt figure was actually a tad low. The national debt, including money owed to investors and foreign governments as well as obligations owed from one federal account to another, was approaching $16.5 trillion -- and has since hit it -- the day he [...]

2. **Fiscal Challenges: Health Care, Taxes and Beyond**
   URL: https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html
   Content: Medicare spending is expected to rise from 2.3% of GDP currently to 7.0% of GDP in 2045, while federal spending on Medicaid (that is, excluding state contributions) will expand from 1.5% to 2.6% of national output. Much of the increase in Medicare spending is driven by per-beneficiary costs rising faster than inflation, even controlling for demographic trends. In sum, the costs to the federal government of the three most important entitlement programs are expected almost to double from 8.0% of GDP today to about 15.6% of GDP in 2045. In 2005, all other spending programs of the federal government, excluding interest payments on the national debt, amounted to 9.0% of GDP. Thus, if the [...]

3. **[PDF] Demographic Headwinds - Aspen Economic Strategy Group**
   URL: https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf
   Content: CBO projects that old-age dependency ratios will steadily rise from 34.2 percent in 2024 to 44.2 percent in 2055, as seen in figure 2. As a result, spending on the major old-age entitlement programs is also projected to continue to grow relative to GDP and is a key contributor to rising deficits and debt in CBO’s projections. The projected growth in old-age entitlement program spending can be attributed to (1) the size of cohorts expected to enter into retirement (due to past fertility rates and immigration), (2) CBO’s expectation that life expectancy will continue to rise, and (3) rising health costs. (Of note, projected future fertility rates do not play much of a role in this [...]

4. **Explaining Federal Spending and Revenue-Wed, 05/21/2025 - 12:00 | Committee for a Responsible Federal Budget**
   URL: https://www.crfb.org/papers/explaining-federal-spending-and-revenue
   Content: Individual taxes accounted for roughly half of all federal revenue, or $2.4 trillion. Payroll taxes, which fund Social Security and Medicare, accounted for about one-third and amounted to $1.7 trillion. Corporate income taxes totaled $530 billion (11 percent), and other sources, such as excise taxes, customs duties, estate taxes, fines and fees, made up 5 percent or $253 billion. Over the next decade, the Congressional Budget Office projects that under current law federal spending will increase from 23.4 percent of GDP in FY 2024 to 24.0 percent by 2035, while revenue will rise from 17.1 percent of GDP in FY 2024 to 18.3 percent by 2035. Over the past 50 years, spending has averaged [...]

5. **Entitlements | Penn Wharton Budget Model**
   URL: https://budgetmodel.wharton.upenn.edu/t/Entitlements/
   Content: Brendan Novak · · 55 min read Automatic Retirement Savings Plans for Low-Income Households Brief Entitlements Healthcare Social Security ## President Biden’s Proposal to Extend the Medicare Trust Fund PWBM estimates that President Biden’s new Medicare proposal would increase the solvency of the Medicare trust fund from the year 2028 to 2053. However, a significant share of that increase comes from redirecting existing (current law) revenue to the trust fund. Another portion comes from unspecific expenditure reductions that lack the details required to score. Counting only new income without unspecified expenditure reductions, we project, as an illustrative alternative, that the HI [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 23. PolitiFact / pf_027 - pants-fire

#### Input
- **Claim:** Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `false`
- **TLDR:** Sources say Canada restricts broadcasting false/misleading news, but not that Fox was banned for lying.
- **Explanation:** PolitiFact (Source 1) says the meme’s “banned for lying” rationale is not verified and that the claim “doesn’t” relate to Fox News; it describes Canadian rules against “false or misleading news” but not a Fox-specific ban for lying. Snopes (Source 2) notes CRTC/Radio Act rules prohibit broadcasting “false or misleading news” and says regulators rejected efforts to repeal that rule, but it does not support the claim that Fox News was banned because it violated a law preventing channels from lying to viewers.
- **Confidence reason:** Two fact-check sources address the meme; neither supports a Fox-specific ban rationale.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2014/jul/14/facebook-posts/fox-news-banned-canada/": "contradicting",
  "https://www.snopes.com/fact-check/canadian-fox/": "neutral",
  "https://www.justice.gc.ca/eng/csj-sjc/pl/charter-charte/c63.html": "neutral",
  "https://www.internetsociety.org/resources/internet-fragmentation/canadas-online-news-act/": "neutral",
  "https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/peace_security-paix_securite/combatt-disinformation-desinformation.aspx?lang=eng": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Is Fox News banned in Canada?**
   URL: https://www.politifact.com/factchecks/2014/jul/14/facebook-posts/fox-news-banned-canada/
   Content: "The (false news) provision has kept Fox News and right wing talk radio out of Canada and helped make Canada a model for liberal democracy and freedom," wrote Kennedy. "As a result of that law, Canadians enjoy high-quality news coverage including the kind of foreign affairs and investigative journalism that flourished in this country before Ronald Reagan abolished the ‘Fairness Doctrine’ in 1987." [...] What Kennedy is likely referring to are provisions in Canadian broadcast policy, include the Radio Act and other policies, that prohibit "any false or misleading news." These provisions against spreading misinformation used to be part of Canada’s criminal code, according to Canadian [...]

2. **Was the Fox News Channel Banned in Canada? | Snopes.com**
   URL: https://www.snopes.com/fact-check/canadian-fox/
   Content: It is true that various sections of CRTC regulations prohibit the broadcasting of "false or misleading news" by radio and television licensees, and that in 2011 the CRTC declined to narrow those regulations to apply only to "news that the licensee knows is false or misleading and that endangers or is likely to endanger the lives, health or safety of the public." [...] Canada's Radio Act requires that "a licenser may not broadcast ... any false or misleading news." The provision has kept Fox News and right-wing talk radio out of Canada and helped make Canada a model for liberal democracy and freedom. As a result of that law, Canadians enjoy high quality news coverage, including the kind [...]

3. **Bill C-63: An Act to enact the Online Harms Act, to amend the Criminal Code, the Canadian Human Rights Act and An Act respecting the mandatory reporting of Internet child pornography by persons who provide an Internet service and to make consequential and related amendments to other Acts**
   URL: https://www.justice.gc.ca/eng/csj-sjc/pl/charter-charte/c63.html
   Content: The following considerations support the consistency with the Charter of the duty to make certain content inaccessible to persons in Canada. Content that sexually victimizes a child or revictimizes a survivor and intimate content communicated without consent is expression that lies far from the core of the guarantee of free expression. Generally, expression that lies far from the core receives less protection under the Charter. Dissemination of some of this content already constitutes an offence under the Criminal Code. The objective of the duty to make this content inaccessible when it has been flagged or otherwise comes to an operator’s attention would be both to mitigate the risk of [...]

4. **Canada’s Online News Act - Internet Society**
   URL: https://www.internetsociety.org/resources/internet-fragmentation/canadas-online-news-act/
   Content: This is just one example of what reducing access to news can do in a crisis situation, but the impact is far greater. Services that aren’t even classified as ‘digital news intermediaries’ are affected. For example, it could make it harder for Canadian contributors to Wikipedia to do research and fact-checking, since this law hinders their ability to discover credible news content online in Canada. People in other countries have easier access to news. This law also poses a fragmentation threat because it centralizes management and restricts the use of links—a basic Internet function—by a centralized authority (CRTC) in Canada. This prevents people and businesses from contributing to the [...]

5. **Combatting foreign disinformation and information manipulation**
   URL: https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/peace_security-paix_securite/combatt-disinformation-desinformation.aspx?lang=eng
   Content: ### Sanctioning disinformation agents Canada has imposed sanctions against individuals and entities that are responsible for spreading false narratives and propaganda. Sanctions – Russian invasion of Ukraine tracks Canada's sanctions against disinformation and propaganda actors in the context of Russian invasion of Ukraine. ## Foreign disinformation and information manipulation Democracies rely on access to diverse, accurate and reliable information and news. This allows citizens and other members of society to develop informed opinions, take part in public debate, and hold governments to account. Information integrity, or the accuracy and reliability of content, enables democratic [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 24. PolitiFact / pf_030 - true

#### Input
- **Claim:** Today California is kicking our butt, creating more jobs and more economic growth than Texas.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact found California outpaced Texas on job growth and economic indicators.
- **Explanation:** PolitiFact’s fact checks on the exact “Today, California is kicking our butt…” claim rated it True and reported California had higher job growth rates and stronger per-capita income/GDP growth than Texas (Sources 1 and 3). A Stanford policy brief also states California’s per-capita income and GDP performance have stood out relative to Texas in recent years (Source 4). However, the PolitiFact update notes California’s job growth had slowed to closer to Texas by late 2016, so the “today” framing is time-dependent (Source 1).
- **Confidence reason:** Directly addressed by PolitiFact; other sources are broader and time-variant.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today California is kicking our butt, creating more jobs and more economic growth than Texas.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/": "supporting",
  "https://www.texasstandard.org/stories/__trashed-4/": "neutral",
  "https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/": "supporting",
  "https://siepr.stanford.edu/publications/policy-brief/tale-two-states-contrasting-economic-policy-california-and-texas": "supporting",
  "https://statspanda.com/blog/texas-vs-california-comparison": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Is California's economy 'growing a hell of a lot faster' than Texas?**
   URL: https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/
   Content: In August, PolitiFact Texas took a deep look at the economies of both California and Texas to evaluate a June claim by Julián Castro, the U.S. secretary of Housing and Urban Development, that "Today, California is kicking our butt, creating more jobs and more economic growth than Texas." It rated the claim True, citing greater jobs, per capita income and GDP growth rates in California. It noted Texas had a lower jobless rate. Building on that fact check, we looked at the most recent economic figures for both states to see if the assessment still holds. [...] California had one more economic bright spot in 2015: Per capita personal income grew at twice the rate as in Texas, 5.4 percent [...]

2. **Is Texas Trailing Behind California on Economic Growth? |  Texas Standard**
   URL: https://www.texasstandard.org/stories/__trashed-4/
   Content: Julián Castro, the U.S. secretary of Housing and Urban Development, brought up California during the Texas Democratic Party’s state convention after noting that as governor, Republican Rick Perry taunted the west coast state for its economy not matching his home state’s pace. “Today,” the former San Antonio mayor told reporters June 17, 2016, “California is kicking our butt, creating more jobs and more economic growth than Texas. Maybe what we need to do is trade in Gov. Jerry Brown,” of California, “for Gov. Greg Abbott and get better results.” Is that a fact? Gardner Selby of the PolitiFact Texas fact-checking team has the answer. [...] “Today,” the former San Antonio mayor told [...]

3. **PolitiFact | Julián Castro says California besting Texas in creating jobs, economic growth**
   URL: https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/
   Content: "Today," the former San Antonio mayor told reporters June 17, 2016, "California is kicking our butt, creating more jobs and more economic growth than Texas. Maybe what we need to do is trade in Gov. Jerry Brown," of California, "for Gov. Greg Abbott and get better results." Castro made a similar declaration in his evening keynote speech, telling delegates: "This is what happens when a party doesn’t believe in government in the first place but has absolute power over its people for decades. You know, they used to brag that Texas was doing so much better than big bad liberal California. But Texas Republicans managed to bungle that too. Because today California is kicking our butt in job [...]

4. **A tale of two states: Contrasting economic policy in California and Texas | Stanford Institute for Economic Policy Research (SIEPR)**
   URL: https://siepr.stanford.edu/publications/policy-brief/tale-two-states-contrasting-economic-policy-california-and-texas
   Content: In light of these population trends during the last decade or two, one might expect other measures of economic performance to show Texas as a rising force and California as a receding one. However, and as shown in Table 1 below, California’s performance stands out when considering the growth in per capita income (PCI) in recent years. Between 2000 and 2020, California’s PCI was significantly greater than both Texas and the U.S. as a whole (BEA, 2021). Both disparities grew substantially from 2015 to 2020. For example, while California’s per capita income was 20 percent higher than Texas’ in 2015, this gap surged to 30 percent just 5 years later. And this was not simply a COVID-induced [...]

5. **Texas vs California: America's Two Largest State Economies Compared by the Data | StatsPanda Blog | StatsPanda**
   URL: https://statspanda.com/blog/texas-vs-california-comparison
   Content: But the story changes when you factor in taxes and cost of living. Texas has no state income tax, while California's top rate of 13.3% is the highest in the nation. A tech worker earning $200,000 in California pays roughly $18,000 in state income tax; the same worker in Texas pays $0. This tax advantage has fueled massive corporate relocations — Tesla, Oracle, Hewlett Packard Enterprise, and Charles Schwab have all moved headquarters from California to Texas. Population growth is the clearest divergence: Texas grew 9.1% from 2020 to 2025, adding nearly 2.5 million people. California's population actually declined by 0.3%, a historic reversal. Texas is now projected to overtake [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

## Arm C - Full Pipeline

Failures shown: 25

### 1. AVeriTeC / av_006 - Not Enough Evidence

#### Input
- **Claim:** Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `15`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say the 2020 ranking was not yet released and the “third” claim used 2019 data.
- **Explanation:** HumAngle and AFP report that the viral claim about Nigeria being third most terrorised in 2020 was misleading because the Global Terrorism Index 2020 ranking had not been released yet and the figures shown were from 2019. FactCheckHub similarly says the infographic labeled “2020” was misleading and used older ranking data, even though it placed Afghanistan and Iraq ahead of Nigeria.
- **Confidence reason:** Multiple fact-checks directly address and refute the 2020 ranking claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/": "contradicting",
  "https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/": "contradicting",
  "https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa": "contradicting",
  "https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism": "neutral",
  "https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **Factcheck: Nigeria Not Ranked Third Most Terrorised Country In 2020 - HumAngle**
   URL: https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/
   Stance: `contradicting`

2. **Misleading 2020 global terrorism ranking resurfaces online - FactCheckHub**
   URL: https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/
   Stance: `contradicting`

3. **Old data circulates claiming Nigeria is the most terrorised country in Africa | Fact Check**
   URL: https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa
   Stance: `contradicting`

4. **Global Terrorism Index 2020: Measuring the impact of terrorism - World | ReliefWeb**
   URL: https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism
   Stance: `neutral`

5. **[PDF] 2024 Global Terrorism Index - Institute for Economics & Peace**
   URL: https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_007 - Not Enough Evidence

#### Input
- **Claim:** Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `20`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources mostly say increased enforcement and barriers can increase smuggling, not decrease it.
- **Explanation:** Source 1 explicitly argues that expanded border enforcement increases human smuggling, citing DHS/USBP findings that smuggler usage rates rose over decades and that enforcement fueled reliance on smugglers. Source 4 similarly finds enforcement can lead to smugglers being used more, with marginal increases in violent crime tied to crossers resorting to smugglers. While Sources 3 and 5 discuss declines in illegal entries, they do not provide evidence about illegal drug activity or human smuggling decreasing specifically in barrier-deployed U.S. areas.
- **Confidence reason:** Direct evidence against the claim appears in Source 1 and 4.
- **Claim verdicts:**
```json
[
  {
    "claim": "Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf": "contradicting",
  "https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers": "neutral",
  "https://cmsny.org/publications/jmhs-is-border-enforcement-effective/": "neutral",
  "https://ccis.ucsd.edu/_files/wp131.pdf": "contradicting",
  "https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025": "neutral"
}
```

#### Pipeline Sources Output
1. **[PDF] nfap policy brief » may 2022 - human smuggling and us immigration ...**
   URL: https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf
   Stance: `contradicting`

2. **The Border Wall System is Deployed, Effective, and Disrupting Criminals and Smugglers | Homeland Security**
   URL: https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers
   Stance: `neutral`

3. **Is Border Enforcement Effective? What We Know and What it Means - The Center for Migration Studies of New York (CMS)**
   URL: https://cmsny.org/publications/jmhs-is-border-enforcement-effective/
   Stance: `neutral`

4. **[PDF] The Effect of Illegal Immigration and Border Enforcement on Crime ...**
   URL: https://ccis.ucsd.edu/_files/wp131.pdf
   Stance: `contradicting`

5. **Border Crossings Once Again at a Record Low in November 2025 | Homeland Security**
   URL: https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The sources don’t provide police-force growth figures since 2002, so the 50% claim can’t be checked.
- **Explanation:** None of the provided sources include data showing how many South African police officers there were in 2002 versus a later year, nor do they state a 50% growth figure. Source 2 discusses police shortages and international comparisons, but it does not give a since-2002 growth percentage. Sources 1 and 4 are annual reports, yet the provided excerpts only list legislation and do not contain the needed staffing-growth statistics.
- **Confidence reason:** No source excerpt contains the required 2002-to-present police growth data.
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf": "neutral",
  "https://groundup.org.za/article/south-africas-police-shortage/": "neutral",
  "https://en.wikipedia.org/wiki/South_African_Police_Service": "neutral",
  "https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf": "neutral",
  "https://en.wikipedia.org/wiki/Crime_in_South_Africa": "neutral"
}
```

#### Pipeline Sources Output
1. **[PDF] south-african-police-service-annual-report-2024-2025.pdf**
   URL: https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf
   Stance: `neutral`

2. **How the size of South Africa’s police force compares to other countries | GroundUp**
   URL: https://groundup.org.za/article/south-africas-police-shortage/
   Stance: `neutral`

3. **South African Police Service - Wikipedia**
   URL: https://en.wikipedia.org/wiki/South_African_Police_Service
   Stance: `neutral`

4. **[PDF] South African Police Service Annual Report 2023/2024**
   URL: https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf
   Stance: `neutral`

5. **Crime in South Africa - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Crime_in_South_Africa
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_010 - Refuted

#### Input
- **Claim:** UNESCO declared Nadar community as the most ancient race in the world.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** None of the sources show UNESCO declaring Nadars the world’s most ancient race.
- **Explanation:** The provided UNESCO-related sources (Source 2 and Source 5) discuss UNESCO’s stance against racial myths and do not mention the Nadar community or any declaration about them. The Nadar-focused sources (Sources 1, 3, 4) discuss Nadar origins and community beliefs, but they do not attribute any “most ancient race in the world” declaration to UNESCO.
- **Confidence reason:** UNESCO declarations about Nadars are not mentioned in any source.
- **Claim verdicts:**
```json
[
  {
    "claim": "UNESCO declared the Nadar community as the most ancient race in the world.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://en.wikipedia.org/wiki/Nadar_(caste)": "neutral",
  "https://www.filosoficas.unam.mx/docs/608/files/4statementsRACE.pdf": "neutral",
  "https://nadars.in/en/nadar-mahajana-sangam/": "neutral",
  "https://www.sanrorhistoricalresearch.com/en/nadar-history-misconceptions/nadar-19th-century-history-misconception/": "neutral",
  "https://courier.unesco.org/en/articles/fallacies-racism-exposed-unesco-publishes-declaration-worlds-scientists": "neutral"
}
```

#### Pipeline Sources Output
1. **Nadar (caste) - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Nadar_(caste)
   Stance: `neutral`

2. **[PDF] Four statements on the race question; UNESCO and its programme**
   URL: https://www.filosoficas.unam.mx/docs/608/files/4statementsRACE.pdf
   Stance: `neutral`

3. **Nadar community | Nadar sangam | Nadars of Tamilnad**
   URL: https://nadars.in/en/nadar-mahajana-sangam/
   Stance: `neutral`

4. **The Actual Social Standing of the 19th-Century Nadars.**
   URL: https://www.sanrorhistoricalresearch.com/en/nadar-history-misconceptions/nadar-19th-century-history-misconception/
   Stance: `neutral`

5. **Fallacies of racism exposed: UNESCO publishes Declaration by world's scientists | The UNESCO Courier**
   URL: https://courier.unesco.org/en/articles/fallacies-racism-exposed-unesco-publishes-declaration-worlds-scientists
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_011 - Supported

#### Input
- **Claim:** Fact Check: WHO has not approved home remedy for COVID-19, don’t fall for misinformation
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** Sources don’t show WHO’s approval status for home remedies.
- **Explanation:** None of the provided sources explicitly state that WHO has not approved home remedies for COVID-19. Source 1 and Source 2 focus on debunking specific purported remedies (e.g., garlic, lemon juice, zinc) but do not address WHO’s formal approval status of “home remedies.” Source 5 discusses WHO-approved therapeutics for patients, not whether WHO has approved any home remedies.
- **Confidence reason:** No source directly addresses WHO approval of home remedies.
- **Claim verdicts:**
```json
[
  {
    "claim": "WHO has not approved home remedies for COVID-19.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://factcheck.afp.com/debunks-novel-coronavirus-prevention-cures-treatments": "neutral",
  "https://www.factcheck.org/covid-misconceptions/": "neutral",
  "https://www.factcheck.org/issue/covid-19-drugs/": "neutral",
  "https://www.factcheck.org/2021/07/scicheck-no-new-revelation-on-hydroxychloroquine-and-covid-19/": "neutral",
  "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/treatments": "neutral"
}
```

#### Pipeline Sources Output
1. **Debunks of novel coronavirus prevention, cures, treatments | Fact Check**
   URL: https://factcheck.afp.com/debunks-novel-coronavirus-prevention-cures-treatments
   Stance: `neutral`

2. **COVID-19 Misconceptions - FactCheck.org**
   URL: https://www.factcheck.org/covid-misconceptions/
   Stance: `neutral`

3. **COVID-19 drugs Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/covid-19-drugs/
   Stance: `neutral`

4. **No New Revelation on Hydroxychloroquine and COVID-19 - FactCheck.org**
   URL: https://www.factcheck.org/2021/07/scicheck-no-new-revelation-on-hydroxychloroquine-and-covid-19/
   Stance: `neutral`

5. **Treatments**
   URL: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/treatments
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_012 - Not Enough Evidence

#### Input
- **Claim:** Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `false`
- **Score:** `10`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say there’s no evidence for the 25,000 child-torture/rape pictures claim.
- **Explanation:** Source 1 (PolitiFact) says there is no evidence supporting the specific Facebook claim that Hunter Biden had “25,000 pics” of torturing/raping children under 10 on his laptop. Source 2 (FactCheck.org) similarly states the meme provides no evidence despite claiming a specific number of images, and notes the broader allegations are baseless. Other sources discuss the laptop containing many personal files and that there was no tampering, but they do not provide support for the specific child-torture/rape content claim.
- **Confidence reason:** Multiple fact-checkers directly reject the exact allegation.
- **Claim verdicts:**
```json
[
  {
    "claim": "Hunter Biden had 25,000 pictures of him torturing and raping children under 10 in China on his laptop.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://dpaq.de/gXxW2": "contradicting",
  "https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/": "contradicting",
  "https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter": "neutral",
  "https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/": "neutral",
  "https://www.nbcnews.com/tech/tech-news/inside-campaign-pizzagate-hunter-biden-n1244331": "neutral"
}
```

#### Pipeline Sources Output
1. **Fact-checking unproven claims about Hunter Biden and child ...**
   URL: https://dpaq.de/gXxW2
   Stance: `contradicting`

2. **Social Media Posts Dredge Up Baseless 'Child Trafficking ...**
   URL: https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/
   Stance: `contradicting`

3. **Hunter Biden laptop letter - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter
   Stance: `neutral`

4. **Copy of what's believed to be Hunter Biden's laptop data turned over ...**
   URL: https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/
   Stance: `neutral`

5. **Inside the campaign to 'pizzagate' Hunter Biden - NBC News**
   URL: https://www.nbcnews.com/tech/tech-news/inside-campaign-pizzagate-hunter-biden-n1244331
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_013 - Refuted

#### Input
- **Claim:** Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `false, mostly_false`
- **TLDR:** The 21-times claim is supported by some medical sources but not by fact-checkers.
- **Explanation:** Source 1 and Source 6 both state that the “21 times a month to avoid prostate cancer” framing is not proven/accurate, contradicting the second and third claims. However, Source 7, Source 10, Source 12, and Source 13 report that men who ejaculated 21+ times per month had a lower prostate cancer risk (about 20–31% lower), which supports the general idea behind the third claim (risk reduction) and partially aligns with the 21-times threshold. The first claim (Dr. Ebeneezer’s job/role at Amuzu Hospital) is only asserted in Source 1 and is not corroborated elsewhere in the provided sources.
- **Confidence reason:** Medical sources support risk reduction; fact-checkers dispute the strict advice framing.
- **Claim verdicts:**
```json
[
  {
    "claim": "Dr. Ebeneezer is a medical doctor and a herbal practitioner at Amuzu Hospital.",
    "verdict": "supported"
  },
  {
    "claim": "Dr. Ebeneezer instructed men to have sex at least 21 times a month.",
    "verdict": "supported"
  },
  {
    "claim": "Having sex at least 21 times a month helps men avoid prostate cancer.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://leadstories.com/hoax-alert/2020/10/fact-check-study-did-not-say-men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer.html": "contradicting",
  "https://www.cui.edu/uploadedfiles/academicprograms/globalprograms/study-abroad/ghana-humanities.pdf": "neutral",
  "https://www.uwindsor.ca/secretariat/sites/uwindsor.ca.secretariat/files/s250530p_-_combined_may_30_2025_senate_package_compressed2.pdf": "neutral",
  "https://documents1.worldbank.org/curated/en/099050923113537780/txt/P1800600a10ae90009f25075bb8a4f8cf8.txt": "neutral",
  "https://www.ug.edu.gh/sites/default/files/manual_uploads/CBAS%20handbook%202017.pdf": "neutral",
  "https://punchng.com/fact-check-does-having-sex-21-times-a-month-prevent-cancer-in-40-years-and-above-men/": "contradicting",
  "https://www.health.harvard.edu/mens-health/ejaculation_frequency_and_prostate_cancer": "supporting",
  "https://howwelove.com/whats-a-healthy-frequency-for-a-couple-to-have-sex/": "neutral"
}
```

#### Pipeline Sources Output
1. **Fact Check: Study Did NOT Say Men Must Have Sex At Least 21 Times A Month To Avoid Prostate Cancer | Lead Stories**
   URL: https://leadstories.com/hoax-alert/2020/10/fact-check-study-did-not-say-men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer.html
   Stance: `contradicting`

2. **UNIVERSITY OF GHANA HANDBOOK FOR THE BACHELOR'S**
   URL: https://www.cui.edu/uploadedfiles/academicprograms/globalprograms/study-abroad/ghana-humanities.pdf
   Stance: `neutral`

3. **[PDF] NOTICE OF MEETING AGENDA - University of Windsor**
   URL: https://www.uwindsor.ca/secretariat/sites/uwindsor.ca.secretariat/files/s250530p_-_combined_may_30_2025_senate_package_compressed2.pdf
   Stance: `neutral`

4. **P1800600a10ae90009f25075bb... - Documents & Reports**
   URL: https://documents1.worldbank.org/curated/en/099050923113537780/txt/P1800600a10ae90009f25075bb8a4f8cf8.txt
   Stance: `neutral`

5. **[PDF] CBAS handbook 2017.pdf - University of Ghana**
   URL: https://www.ug.edu.gh/sites/default/files/manual_uploads/CBAS%20handbook%202017.pdf
   Stance: `neutral`

6. **FACT CHECK: Does having sex 21 times a month prevent cancer in 40 years and above men?**
   URL: https://punchng.com/fact-check-does-having-sex-21-times-a-month-prevent-cancer-in-40-years-and-above-men/
   Stance: `contradicting`

7. **Ejaculation frequency and prostate cancer - Harvard Health**
   URL: https://www.health.harvard.edu/mens-health/ejaculation_frequency_and_prostate_cancer
   Stance: `supporting`

8. **What’s A Healthy Frequency for A Couple to Have Sex? – How We Love**
   URL: https://howwelove.com/whats-a-healthy-frequency-for-a-couple-to-have-sex/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_016 - Not Enough Evidence

#### Input
- **Claim:** You see the number today? 33.1 GDP. The biggest in the history of our country by almost triple, right? Almost triple. Now it’s very much bigger than any GDP we’ve ever had. You have to go back to the 1950s, and then it’s less than half. This is the greatest number, 33.1 percent.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `25`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources only support the 33.1% growth rate, not the other “biggest ever” comparisons.
- **Explanation:** Sources 1, 2, 6, and 7 clearly support that U.S. GDP growth was 33.1% (annualized) in Q3 2020, but they do not support the claims that this is the biggest GDP in the country’s history “by almost triple” or “very much bigger than any GDP the country has ever had.” Source 6 and 8 explicitly contradict the “biggest and best in history” framing, noting it’s the fastest quarterly increase and that it follows record-breaking losses. The remaining claims about needing to go back to the 1950s for values less than half, and that “33.1 percent is the greatest number,” are not supported by the provided sources.
- **Confidence reason:** Some claims directly addressed; others lack necessary historical comparisons.
- **Claim verdicts:**
```json
[
  {
    "claim": "The number today is 33.1 GDP.",
    "verdict": "supported"
  },
  {
    "claim": "33.1 GDP is the biggest in the history of the country by almost triple.",
    "verdict": "contradicted"
  },
  {
    "claim": "33.1 GDP is very much bigger than any GDP the country has ever had.",
    "verdict": "contradicted"
  },
  {
    "claim": "To find a GDP value less than half of 33.1, you have to go back to the 1950s.",
    "verdict": "unverifiable"
  },
  {
    "claim": "33.1 percent is the greatest number.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html": "supporting",
  "https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068": "neutral",
  "https://www.factcheck.org/issue/gdp/": "neutral",
  "https://www.factcheck.org/2026/04/trumps-numbers-april-2026-update/": "neutral",
  "https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-4th": "neutral",
  "https://www.cnn.com/2020/10/29/economy/gdp-report-trump-biggest-best-factcheck": "contradicting",
  "https://www.bbc.com/news/world-45827430": "contradicting",
  "https://www.politifact.com/factchecks/2020/oct/01/donald-trump/donald-trumps-dubious-statement-about-presiding-ov/": "contradicting"
}
```

#### Pipeline Sources Output
1. **U.S. GDP booms at 33.1% rate in Q3 report, beating expectations**
   URL: https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html
   Stance: `supporting`

2. **GDP rose at 33.1 percent annualized rate last quarter, but blowout figure is not what it seems**
   URL: https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068
   Stance: `neutral`

3. **GDP Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/gdp/
   Stance: `neutral`

4. **Trump's Numbers, April 2026 Update - FactCheck.org**
   URL: https://www.factcheck.org/2026/04/trumps-numbers-april-2026-update/
   Stance: `neutral`

5. **GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 4th Quarter and Year 2025 | U.S. Bureau of Economic Analysis (BEA)**
   URL: https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-4th
   Stance: `neutral`

6. **GDP Report: Trump is taking credit for the ‘biggest and best’ GDP in American history. Here are the facts | CNN Business**
   URL: https://www.cnn.com/2020/10/29/economy/gdp-report-trump-biggest-best-factcheck
   Stance: `contradicting`

7. **US 2020 election: The economy under Trump in six charts**
   URL: https://www.bbc.com/news/world-45827430
   Stance: `contradicting`

8. **PolitiFact | Donald Trump’s dubious statement about presiding over ‘the greatest economy’ in history**
   URL: https://www.politifact.com/factchecks/2020/oct/01/donald-trump/donald-trumps-dubious-statement-about-presiding-ov/
   Stance: `contradicting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_017 - Supported

#### Input
- **Claim:** Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true, mostly_true`
- **TLDR:** Sources do not support a specific loss of 300,000 manufacturing jobs from the China trade war.
- **Explanation:** Source 1 mentions Moody’s estimating the trade conflict with China reduced U.S. employment by 300,000 jobs, but it does not specify that these were manufacturing jobs. Source 3 instead reports estimates of job losses that are smaller than 300,000 and frames the effect as net negative for manufacturing employment, not as a clear 300,000 manufacturing-job loss. Source 2 finds no evidence of net U.S. job losses from the “China shock” overall, further undermining the claim’s premise.
- **Confidence reason:** 300,000 figure appears only for overall employment, not manufacturing.
- **Claim verdicts:**
```json
[
  {
    "claim": "Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.statesman.com/story/news/politics/elections/2020/07/01/fact-check-did-trump-lose-trade-war-that-he-started-per-biden-ad/113740186/": "supporting",
  "https://sccei.fsi.stanford.edu/china-briefs/did-china-shock-cause-widespread-job-losses-us": "contradicting",
  "https://econofact.org/factbrief/did-the-trump-tariffs-increase-us-manufacturing-jobs": "contradicting",
  "https://www.cato.org/blog/manufacturing-employment-data-confirms-concentrated-benefits-dispersed-costs-trumps-tariffs": "neutral",
  "https://www.progressivepolicy.org/u-s-manufacturing-employment-is-down-108000-in-2025/": "neutral"
}
```

#### Pipeline Sources Output
1. **Fact-check: Did Trump lose a trade war that he started, per Biden ad?**
   URL: https://www.statesman.com/story/news/politics/elections/2020/07/01/fact-check-did-trump-lose-trade-war-that-he-started-per-biden-ad/113740186/
   Stance: `supporting`

2. **Did the “China Shock” Cause Widespread Job Losses in the U.S.? | FSI**
   URL: https://sccei.fsi.stanford.edu/china-briefs/did-china-shock-cause-widespread-job-losses-us
   Stance: `contradicting`

3. **Fact Check: Did the Trump tariffs increase US manufacturing jobs? | Econofact**
   URL: https://econofact.org/factbrief/did-the-trump-tariffs-increase-us-manufacturing-jobs
   Stance: `contradicting`

4. **Manufacturing Employment Data Confirm the Concentrated Benefits—and Dispersed Costs—of Trump’s Tariffs | Cato at Liberty Blog**
   URL: https://www.cato.org/blog/manufacturing-employment-data-confirms-concentrated-benefits-dispersed-costs-trumps-tariffs
   Stance: `neutral`

5. **U.S. manufacturing employment is down 108,000 in 2025**
   URL: https://www.progressivepolicy.org/u-s-manufacturing-employment-is-down-108000-in-2025/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_020 - Supported

#### Input
- **Claim:** Edo State in Nigeria has a 19% unemployment rate.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `true, mostly_true`
- **TLDR:** Only one source reports Edo’s unemployment at 19%; others don’t confirm.
- **Explanation:** Source 1 (Dubawa) reports that Godwin Obaseki claimed Edo’s unemployment fell from 25% to 19% and says this was verifiable with an NBS report, but the source excerpt does not provide the underlying NBS state figure itself. The other sources provided do not give Edo’s unemployment rate as 19% (Source 5 is for Q3 2018 and is not quoted; Sources 2–4 discuss national unemployment or other figures without confirming Edo=19%).
- **Confidence reason:** Edo=19% is only asserted indirectly in one source.
- **Claim verdicts:**
```json
[
  {
    "claim": "Edo State in Nigeria has a 19% unemployment rate.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/": "supporting",
  "https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf": "neutral",
  "https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/": "neutral",
  "https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria": "neutral",
  "https://www.nigerianstat.gov.ng/elibrary/read/929": "neutral"
}
```

#### Pipeline Sources Output
1. **Is Edo unemployment rate 19 percent as claimed by Obaseki? - Dubawa**
   URL: https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/
   Stance: `supporting`

2. **[PDF] perception of edo residents towards unemployment**
   URL: https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf
   Stance: `neutral`

3. **How true are viral claims on Nigeria’s unemployment rate, extreme poverty and debt profile? | The ICIR- Latest News, Politics, Governance, Elections, Investigation, Factcheck, Covid-19**
   URL: https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/
   Stance: `neutral`

4. **12 Unemployment Statistics in Nigeria for 2026 | MyJobMag**
   URL: https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria
   Stance: `neutral`

5. **Reports | National Bureau of Statistics**
   URL: https://www.nigerianstat.gov.ng/elibrary/read/929
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. AVeriTeC / av_021 - Not Enough Evidence

#### Input
- **Claim:** Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `25`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** A fact-check says Saudi petrol was more expensive than Nigeria, contradicting the 40% claim.
- **Explanation:** Source 1 directly evaluates the “40% cheaper in Nigeria than in Saudi Arabia” claim and concludes it is an exaggeration, stating Saudi petrol was 17.78% (octane 95) and 11.16% (octane 91) more expensive than Nigeria after currency conversion. The other sources either don’t provide comparable 2020 price data (Source 2) or discuss a different comparison context (Source 3) or general/other-year gasoline prices (Sources 4 and 5), so they don’t overturn Source 1’s contradiction.
- **Confidence reason:** Only one source directly tests the specific 40% claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/": "contradicting",
  "https://www.facebook.com/groups/599563341561133/posts/1445300556987403/": "neutral",
  "https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/": "neutral",
  "https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf": "neutral",
  "https://tradingeconomics.com/country-list/gasoline-prices": "neutral"
}
```

#### Pipeline Sources Output
1. **FACT CHECK: Is petrol 40% cheaper in Nigeria than in Saudi Arabia as claimed by Dangote? - TheCable Fact Check**
   URL: https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/
   Stance: `contradicting`

2. **Fuel price comparison between Saudi Arabia and Nigeria - Facebook**
   URL: https://www.facebook.com/groups/599563341561133/posts/1445300556987403/
   Stance: `neutral`

3. **FG justifies fuel price comparison with Saudi Arabia, others | Multiplatform Digital Information Technology**
   URL: https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/
   Stance: `neutral`

4. **[PDF] Fossil fuel subsidy swaps: A path towards accelerating the ...**
   URL: https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf
   Stance: `neutral`

5. **Gasoline Prices - Countries - List**
   URL: https://tradingeconomics.com/country-list/gasoline-prices
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. AVeriTeC / av_022 - Refuted

#### Input
- **Claim:** The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** None of the sources show Nigeria donating $600M to Biden’s campaign.
- **Explanation:** The Washington Examiner article discusses a $600 million unemployment-funds fraud involving Nigerian scammers, and mentions donations to Biden, but it does not say the Nigerian government donated $600 million to Joe Biden’s campaign. The other sources discuss U.S. assistance to Nigeria against Boko Haram (whitehouse.gov) and foreign donations to Trump (PBS), plus unrelated material; none provide evidence for the specific claim about a $600 million Nigerian government donation to Biden.
- **Confidence reason:** No source directly addresses the specific donation claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/": "neutral",
  "https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues": "neutral",
  "https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-": "neutral",
  "https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/": "neutral",
  "https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **Biden pick for unemployment program lost $600M to Nigerian scammers**
   URL: https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/
   Stance: `neutral`

2. **Trump wants to investigate Democrats' fundraising, but his own campaign has issues | PBS News**
   URL: https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues
   Stance: `neutral`

3. **FACT SHEET: U.S. Efforts to Assist the Nigerian Government in its Fight against Boko Haram | whitehouse.gov**
   URL: https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-
   Stance: `neutral`

4. **KOCO 5 News**
   URL: https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/
   Stance: `neutral`

5. **[PDF] Congress Must Stop Biden's Misuse of U.S. Foreign Aid to Impose ...**
   URL: https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 13. AVeriTeC / av_027 - Refuted

#### Input
- **Claim:** The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `true`
- **Score:** `95`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `true`, expected one of `false, mostly_false`
- **TLDR:** The claim is fake; multiple fact-checks say no such shootdown occurred.
- **Explanation:** All provided sources directly address the viral allegation and state it is false. Newschecker says the claim is fake and that no such incident has taken place, and Latestly reports that India’s Press Information Bureau (PIB) debunked the same tweet as untrue. Vishvas News similarly concludes the viral post is fake and notes IAF denied the claim.
- **Confidence reason:** Multiple fact-checks and PIB debunk the shootdown claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://newschecker.in/fact-check/pla-did-not-shoot-down-indian-fighter-jet-sukhoi-su-30-in-tibet": "contradicting",
  "https://www.latestly.com/social-viral/fact-check/iaf-sukhoi-su-30-fighter-jet-was-not-shot-down-by-chinas-pla-in-tibet-pib-debunks-fake-news-2066857.html": "contradicting",
  "https://www.instagram.com/p/CF6t5R3DEn8/": "contradicting",
  "https://x.com/PIBFactCheck/status/1312692937898119169": "contradicting",
  "https://www.vishvasnews.com/english/politics/fact-check-iafs-sukhoi-30-jet-was-not-shot-down-in-tibet-viral-claim-is-fake/": "contradicting"
}
```

#### Pipeline Sources Output
1. **PLA Did Not Shoot Down Indian Fighter Jet Sukhoi Su–30 In Tibet - Newschecker**
   URL: https://newschecker.in/fact-check/pla-did-not-shoot-down-indian-fighter-jet-sukhoi-su-30-in-tibet
   Stance: `contradicting`

2. **IAF Sukhoi Su-30 Fighter Jet Was Not Shot Down by China's PLA in Tibet; PIB Debunks Fake News | 🔎 LatestLY**
   URL: https://www.latestly.com/social-viral/fact-check/iaf-sukhoi-su-30-fighter-jet-was-not-shot-down-by-chinas-pla-in-tibet-pib-debunks-fake-news-2066857.html
   Stance: `contradicting`

3. **Instagram**
   URL: https://www.instagram.com/p/CF6t5R3DEn8/
   Stance: `contradicting`

4. **A tweet claims that an IAF Sukhoi Su-30 fighter jet has been shot ...**
   URL: https://x.com/PIBFactCheck/status/1312692937898119169
   Stance: `contradicting`

5. **Fact Check: IAF’s Sukhoi-30 jet shot down in Tibet? No, viral claim is fake**
   URL: https://www.vishvasnews.com/english/politics/fact-check-iafs-sukhoi-30-jet-was-not-shot-down-in-tibet-viral-claim-is-fake/
   Stance: `contradicting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 14. AVeriTeC / av_029 - Refuted

#### Input
- **Claim:** Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `false, mostly_false`
- **TLDR:** Trump suspended China travel early, but sources don’t support it as “unprecedented” or “all travel.”
- **Explanation:** Source 5 (the White House proclamation) shows the U.S. confirmed person-to-person spread in the U.S. and that the proclamation was issued Jan. 31, 2020, with the stated purpose of suspending entry for certain non-U.S. persons who had been in mainland China in the prior 14 days—so it supports that a suspension occurred before the first U.S. person-to-person transmission was confirmed. However, Source 6 (FactCheck.org) says Trump’s claim that he “closed up” all travel was wrong and that there were exceptions, contradicting the “suspended all travel” wording. For “unprecedented,” none of the provided sources establish that the action was uniquely unprecedented; Source 6 notes many other countries imposed restrictions before or on the same day.
- **Confidence reason:** Direct timing is supported, but “all travel” and “unprecedented” are not.
- **Claim verdicts:**
```json
[
  {
    "claim": "Before the first case of coronavirus spread within the United States, President Donald Trump suspended all travel from China.",
    "verdict": "mixed"
  },
  {
    "claim": "President Donald Trump took unprecedented action by suspending all travel from China.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.factcheck.org/2020/03/the-facts-on-trumps-travel-restrictions/": "neutral",
  "https://www.factcheck.org/2020/04/trumps-snowballing-china-travel-claim/": "neutral",
  "https://www.snopes.com/fact-check/trump-ban-travel-china-pandemic/": "neutral",
  "https://www.statesman.com/story/news/politics/elections/2020/04/13/fact-check-was-trump-slow-to-halt-travel-from-china/1361149007/": "neutral",
  "https://trumpwhitehouse.archives.gov/presidential-actions/proclamation-suspension-entry-immigrants-nonimmigrants-persons-pose-risk-transmitting-2019-novel-coronavirus/": "supporting",
  "https://www.factcheck.org/2020/04/trump-biden-spin-china-travel-restrictions/": "contradicting"
}
```

#### Pipeline Sources Output
1. **The Facts on Trump's Travel Restrictions - FactCheck.org**
   URL: https://www.factcheck.org/2020/03/the-facts-on-trumps-travel-restrictions/
   Stance: `neutral`

2. **Trump's Snowballing China Travel Claim - FactCheck.org**
   URL: https://www.factcheck.org/2020/04/trumps-snowballing-china-travel-claim/
   Stance: `neutral`

3. **Did Trump Ban All Travel From China at the Start of the Pandemic? | Snopes.com**
   URL: https://www.snopes.com/fact-check/trump-ban-travel-china-pandemic/
   Stance: `neutral`

4. **Fact-check: Was Trump slow to halt travel from China?**
   URL: https://www.statesman.com/story/news/politics/elections/2020/04/13/fact-check-was-trump-slow-to-halt-travel-from-china/1361149007/
   Stance: `neutral`

5. **Proclamation on Suspension of Entry as Immigrants and ...**
   URL: https://trumpwhitehouse.archives.gov/presidential-actions/proclamation-suspension-entry-immigrants-nonimmigrants-persons-pose-risk-transmitting-2019-novel-coronavirus/
   Stance: `supporting`

6. **Trump, Biden Spin China Travel Restrictions - FactCheck.org**
   URL: https://www.factcheck.org/2020/04/trump-biden-spin-china-travel-restrictions/
   Stance: `contradicting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 15. PolitiFact / pf_003 - true

#### Input
- **Claim:** Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources indicate Hatch co-sponsored a 1993 health bill containing an individual mandate.
- **Explanation:** PolitiFact states that Hatch was the co-sponsor of a 1993 Republican-backed bill that included an individual mandate (Source 1). Fox News also says the idea appeared in two 1993 bills and lists Orrin Hatch among the supporters (Source 2), while the New Yorker describes the mandate’s 1993 legislative debut and notes Hatch as a co-sponsor of a related bill (Source 3). None of the provided sources contradict the claim.
- **Confidence reason:** Multiple sources support, but details of the exact bill are not fully consistent across sources.
- **Claim verdicts:**
```json
[
  {
    "claim": "Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/": "supporting",
  "https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long": "supporting",
  "https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate": "supporting",
  "https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf": "neutral",
  "https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Hatch once supported an individual mandate, said Cenk Uygur**
   URL: https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/
   Stance: `supporting`

2. **Individual health care insurance mandate has roots two decades long | Fox News**
   URL: https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long
   Stance: `supporting`

3. **Unpopular Mandate | The New Yorker**
   URL: https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate
   Stance: `supporting`

4. **[PDF] The New Bipartisan Consensus for an Individual Mandate**
   URL: https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf
   Stance: `neutral`

5. **How Sen. Orrin Hatch Changed America's Health Care - KFF Health News**
   URL: https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 16. PolitiFact / pf_004 - barely-true

#### Input
- **Claim:** Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** None of the sources mention Mark Herring or any vote on shorter sentences for sex offenders.
- **Explanation:** The provided sources discuss sex-offender recidivism generally (Source 1), sex-offense prevalence and reporting (Source 2), Canadian bail/sentencing reforms unrelated to Mark Herring (Source 3), and an Ohio dissent report referencing the Supreme Court case name “Herring” (Source 4). None of the sources contain information about Mark Herring voting to allow sex offenders, including rapists, to serve shorter sentences.
- **Confidence reason:** No source addresses the specific person, vote, or sentencing change.
- **Claim verdicts:**
```json
[
  {
    "claim": "Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf": "neutral",
  "https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf": "neutral",
  "https://openparliament.ca/bills/45-1/C-14/?singlepage=1": "neutral",
  "https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf": "neutral",
  "https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **[PDF] Recidivism: The Great Lie of “Frightening and High” - Regulations.gov**
   URL: https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf
   Stance: `neutral`

2. **[PDF] Sex Offender Management Assessment and Planning Initiative**
   URL: https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf
   Stance: `neutral`

3. **Bill C-14 | openparliament.ca**
   URL: https://openparliament.ca/bills/45-1/C-14/?singlepage=1
   Stance: `neutral`

4. **[PDF] DISSENTING REPORT - Supreme Court of Ohio**
   URL: https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf
   Stance: `neutral`

5. **[PDF] Recommendations for SSOSA reforms; treatment alternatives for ...**
   URL: https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 17. PolitiFact / pf_009 - true

#### Input
- **Claim:** The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources support that Nazis used “untermensch”/“mongrel” dehumanizing language tied to genocide justification.
- **Explanation:** PolitiFact (Source 1) reports that Nazi terms “untermensch” (“subhuman”) and “mischling” (“mongrel”) were part of Nazi propaganda and includes a quote from a Nazi SS leader discussing a struggle between “man” and the “subhuman,” in the context of Nazi antisemitic ideology. PolitiFact also states that Blitzer’s cited phrase was used by Nazis to justify genocide of Jews, and it is rated “true” in PolitiFact’s list (Source 4). The New Yorker and Slate discuss Nugent’s slur and its Nazi echoes but do not independently document Nazi use of the exact phrase “subhuman mongrel” as a justification; they mainly contextualize the slur’s racist/dehumanizing nature.
- **Confidence reason:** Direct Nazi-lexicon support from PolitiFact; exact-phrase genocide link not fully evidenced elsewhere.
- **Claim verdicts:**
```json
[
  {
    "claim": "The words \"subhuman mongrel,\" which Ted Nugent called President Barack Obama, were used by the Nazis.",
    "verdict": "supported"
  },
  {
    "claim": "The Nazis used those words to justify the genocide of the Jewish community.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2014/feb/19/wolf-blitzer/wolf-blitzer-ted-nugent-used-nazi-terminology-subh/": "supporting",
  "https://www.newyorker.com/news/amy-davidson/ted-nugents-subhuman-mongrel-slur-in-translation": "neutral",
  "https://slate.com/human-interest/2014/02/ted-nugent-the-rocker-and-political-activist-referred-to-president-obama-as-a-subhuman-mongrel-in-an-interview-with-guns-com.html": "neutral",
  "https://www.politifact.com/factchecks/list/?target=ted-nugent": "supporting",
  "https://www.tampabay.com/news/politics/national/punditfact-ted-nugents-remarks-about-obama-hark-back-to-nazis/2167186/": "neutral",
  "https://encyclopedia.ushmm.org/content/en/article/deceiving-the-public": "neutral",
  "https://museumoftolerance.com/learn/educator-resources/what-is-holocaust-denial": "neutral",
  "https://en.wikipedia.org/wiki/Holocaust_denial": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Wolf Blitzer: Ted Nugent used Nazi terminology, 'subhuman mongrel,' to describe President Barack Obama**
   URL: https://www.politifact.com/factchecks/2014/feb/19/wolf-blitzer/wolf-blitzer-ted-nugent-used-nazi-terminology-subh/
   Stance: `supporting`

2. **Ted Nugent’s “Subhuman Mongrel” Slur, in Translation | The New Yorker**
   URL: https://www.newyorker.com/news/amy-davidson/ted-nugents-subhuman-mongrel-slur-in-translation
   Stance: `neutral`

3. **Ted Nugent: The rocker and political activist referred to President Obama as a subhuman mongrel in an interview with Guns.com.**
   URL: https://slate.com/human-interest/2014/02/ted-nugent-the-rocker-and-political-activist-referred-to-president-obama-as-a-subhuman-mongrel-in-an-interview-with-guns-com.html
   Stance: `neutral`

4. **Fact-checks | PolitiFact**
   URL: https://www.politifact.com/factchecks/list/?target=ted-nugent
   Stance: `supporting`

5. **PunditFact: Ted Nugent's remarks about Obama hark back to Nazis**
   URL: https://www.tampabay.com/news/politics/national/punditfact-ted-nugents-remarks-about-obama-hark-back-to-nazis/2167186/
   Stance: `neutral`

6. **Deceiving the Public | Holocaust Encyclopedia**
   URL: https://encyclopedia.ushmm.org/content/en/article/deceiving-the-public
   Stance: `neutral`

7. **What is Holocaust Denial? | Educator Resources | MOT**
   URL: https://museumoftolerance.com/learn/educator-resources/what-is-holocaust-denial
   Stance: `neutral`

8. **Holocaust denial - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Holocaust_denial
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 18. PolitiFact / pf_011 - true

#### Input
- **Claim:** Says Donald Trump has changed his mind on abortion.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Multiple sources say Trump shifted abortion positions, including moving away from a national ban.
- **Explanation:** Axios and Al Jazeera both describe Trump’s shifting abortion stance, including moving toward leaving abortion limits to states and not endorsing a national ban. FactCheck.org similarly states that Trump said he won’t sign a national abortion ban, contrasting with his 2016 support for a federal ban. While the sources don’t prove a single “changed his mind” moment, they consistently document changes over time.
- **Confidence reason:** Several sources document shifts, but not one definitive moment.
- **Claim verdicts:**
```json
[
  {
    "claim": "Donald Trump has changed his mind on abortion.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.axios.com/2024/04/08/trump-abortion-ban-rights-legislation-timeline": "supporting",
  "https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed": "supporting",
  "https://www.aclu.org/trump-on-abortion": "supporting",
  "https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/": "supporting",
  "https://www.congress.gov/118/meeting/house/117301/documents/HHRG-118-FD00-20240515-SD001.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **Trump abortion timeline: Trump changes stance on national abortion rights**
   URL: https://www.axios.com/2024/04/08/trump-abortion-ban-rights-legislation-timeline
   Stance: `supporting`

2. **'Let states decide': How Donald Trump's position on abortion has ...**
   URL: https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed
   Stance: `supporting`

3. **Trump on Abortion | American Civil Liberties Union**
   URL: https://www.aclu.org/trump-on-abortion
   Stance: `supporting`

4. **Trump's 'Like It or Not' Comment and Harris' Response**
   URL: https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/
   Stance: `supporting`

5. **[PDF] Fact-checking 32 of his false claims to Time | CNN Politics**
   URL: https://www.congress.gov/118/meeting/house/117301/documents/HHRG-118-FD00-20240515-SD001.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 19. PolitiFact / pf_016 - half-true

#### Input
- **Claim:** John McCain "has threatened extinction for North Korea and sung songs about bombing Iran."
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `true`
- **Score:** `92`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `true`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources support both McCain’s “extinction” warning on North Korea and his “Bomb Iran” song joke.
- **Explanation:** Multiple sources (Presstv, Legal Reader, and CBS News) report McCain warning that North Korea’s aggression would lead to its “extinction.” For the Iran claim, NPR, CBS News, CNN, and NBC News describe McCain joking/singing “Bomb Iran” by parodying the Beach Boys’ “Barbara Ann.”
- **Confidence reason:** Multiple independent sources directly describe both statements.
- **Claim verdicts:**
```json
[
  {
    "claim": "John McCain has threatened extinction for North Korea.",
    "verdict": "supported"
  },
  {
    "claim": "John McCain has sung songs about bombing Iran.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.presstv.ir/Detail/2017/09/10/534708/US-McCain-North-Korea-nuclear-war-cancer-Kim": "supporting",
  "https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction/": "supporting",
  "https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction": "supporting",
  "https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction/": "supporting",
  "https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction": "supporting",
  "https://www.npr.org/2007/04/20/9688222/jesting-mccain-sings-bomb-bomb-bomb-iran": "supporting",
  "https://www.cbsnews.com/news/iran-laughs-off-mccains-bomb-iran-song/": "supporting",
  "https://www.cnn.com/POLITICS/blogs/politicalticker/2007/04/mccain-sings-bomb-bomb-iran.html": "supporting"
}
```

#### Pipeline Sources Output
1. **McCain threatens North Korea with ‘extinction’**
   URL: https://www.presstv.ir/Detail/2017/09/10/534708/US-McCain-North-Korea-nuclear-war-cancer-Kim
   Stance: `supporting`

2. **Senator John McCain Says North Korea Nuclear Tests Could Lead to Its 'Extintion' - Legal Reader**
   URL: https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction/
   Stance: `supporting`

3. **Senator John McCain Says North Korea Nuclear Tests Could Lead to Its 'Extintion' - Legal Reader**
   URL: https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction
   Stance: `supporting`

4. **McCain to North Korea: aggression will lead to "extinction" - CBS News**
   URL: https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction/
   Stance: `supporting`

5. **McCain to North Korea: aggression will lead to "extinction" - CBS News**
   URL: https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction
   Stance: `supporting`

6. **Jesting, McCain Sings: 'Bomb, Bomb, Bomb' Iran : NPR**
   URL: https://www.npr.org/2007/04/20/9688222/jesting-mccain-sings-bomb-bomb-bomb-iran
   Stance: `supporting`

7. **Iran Laughs Off McCain's "Bomb Iran" Song - CBS News**
   URL: https://www.cbsnews.com/news/iran-laughs-off-mccains-bomb-iran-song/
   Stance: `supporting`

8. **CNN.com - CNN Political Ticker**
   URL: https://www.cnn.com/POLITICS/blogs/politicalticker/2007/04/mccain-sings-bomb-bomb-iran.html
   Stance: `supporting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 20. PolitiFact / pf_017 - true

#### Input
- **Claim:** In the last 10 years, Georgias middle class income has dropped $6,500.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `70`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact supports the $6,500 drop claim using Census data; other sources only partially address it.
- **Explanation:** Source 1 directly evaluates the statement that “In the last 10 years, Georgia’s middle class income has dropped $6,500” and says it is “on target with the Census Bureau data,” citing a $6,500, 10-year drop in household income. Source 2 provides different Census-based figures (median household income $54,803 in 2002 vs. $47,829 in 2013), which is a decline but not explicitly framed as a $6,500 “middle class” drop over the same period. The other sources do not provide Georgia middle-class income change figures comparable to the $6,500 claim.
- **Confidence reason:** Only one source directly checks the exact $6,500 claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the last 10 years, Georgia's middle class income has dropped by $6,500.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/": "supporting",
  "https://saportareport.com/georgias-middle-class-disappearing-gsu-report-cant-say-went/columnists/david/": "neutral",
  "https://thecurrentga.org/2025/10/11/analysis-how-georgias-drop-in-per-capita-income-presaged-its-rural-demographic-collapse-part-2/": "neutral",
  "https://abc45.com/news/nation-world/middle-income-families-struggle-as-living-costs-outpace-dropping-prices-budget-groceries-rent-finances-united-states-economy-fact-check-team": "neutral",
  "https://www.incomebyzipcode.com/georgia": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Carter claim about median household income on target**
   URL: https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/
   Stance: `supporting`

2. **Georgia’s middle class is disappearing; GSU report can’t say where it's going, or why - SaportaReport**
   URL: https://saportareport.com/georgias-middle-class-disappearing-gsu-report-cant-say-went/columnists/david/
   Stance: `neutral`

3. **Analysis: How Georgia’s drop in per capita income presaged its rural demographic collapse – Part 2 - The Current**
   URL: https://thecurrentga.org/2025/10/11/analysis-how-georgias-drop-in-per-capita-income-presaged-its-rural-demographic-collapse-part-2/
   Stance: `neutral`

4. **Fact Check Team: Middle-income families struggle as living costs outpace dropping prices**
   URL: https://abc45.com/news/nation-world/middle-income-families-struggle-as-living-costs-outpace-dropping-prices-budget-groceries-rent-finances-united-states-economy-fact-check-team
   Stance: `neutral`

5. **Georgia Income Statistics | Current Census Data for Georgia Zip Codes**
   URL: https://www.incomebyzipcode.com/georgia
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 21. PolitiFact / pf_018 - half-true

#### Input
- **Claim:** Oil production is down 14 percent this year on federal land.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources discuss overall U.S. crude forecasts, not a 14% drop on federal land.
- **Explanation:** None of the provided sources state that oil production is down 14% this year specifically on federal land. Source 5 (EIA) forecasts U.S. crude production averaging 13.5 million b/d in 2026, about 100,000 b/d less than 2025, and mentions Federal Gulf of America as part of the forecast, but it does not quantify a 14% year-over-year decline on federal land. Sources 1 and 4 similarly discuss EIA forecasts of modest declines in total U.S. crude production, without the specific “14 percent on federal land this year” figure.
- **Confidence reason:** No source provides the specific 14% federal-land figure.
- **Claim verdicts:**
```json
[
  {
    "claim": "Oil production is down 14 percent this year on federal land.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/": "neutral",
  "https://www.factcheck.org/issue/oil-production/": "neutral",
  "https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/": "neutral",
  "https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/": "neutral",
  "https://www.eia.gov/todayinenergy/detail.php?id=66844": "neutral"
}
```

#### Pipeline Sources Output
1. **EIA Sees USA Crude Oil Production Dropping in 2026, 2027 | Rigzone**
   URL: https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/
   Stance: `neutral`

2. **oil production Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/oil-production/
   Stance: `neutral`

3. **EIA sees 2026 oil production decline despite regional growth EIA sees 2026 oil production decline despite regional growth**
   URL: https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/
   Stance: `neutral`

4. **U.S. energy agency forecasts a modest dip in domestic crude production in 2026**
   URL: https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/
   Stance: `neutral`

5. **EIA forecasts U.S. crude oil production will decrease slightly in 2026 - U.S. Energy Information Administration (EIA)**
   URL: https://www.eia.gov/todayinenergy/detail.php?id=66844
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 22. PolitiFact / pf_020 - pants-fire

#### Input
- **Claim:** U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence."
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false`
- **TLDR:** PolitiFact reports Langevin opposed a border fence out of fear someone would get hurt.
- **Explanation:** Source 1 (PolitiFact) directly attributes to Michael J. Gardiner a statement that Langevin opposed a border fence because he was afraid someone would get hurt trying to go around it. Source 3 (OnTheIssues) indicates Langevin voted NO on building a fence, but it does not provide the specific “afraid someone would get hurt” rationale. The other sources provided do not address this specific fear-based justification.
- **Confidence reason:** Specific rationale appears only in one source; other sources lack it.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration.",
    "verdict": "supported"
  },
  {
    "claim": "Jim Langevin said he opposed a border fence because he was afraid someone would get hurt trying to go around the fence.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/": "supporting",
  "https://www.politifact.com/search/factcheck/?q=Trang%20ch%E1%BB%A7%20D%E1%BA%ABn%20l%C6%B0u%20m%C3%A0n%20h%C3%ACnh%20b%C3%A1%20ch%E1%BB%A7%28TG%3Ae10838%29.frm": "neutral",
  "https://www.ontheissues.org/house/James_Langevin_Immigration.htm": "neutral",
  "https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm": "neutral",
  "https://www.congress.gov/event/116th-congress/house-event/LC64036/text": "neutral",
  "https://www.politifact.com/factchecks/2017/apr/23/mick-mulvaney/fact-check-did-top-democrats-vote-border-wall-2006/": "neutral",
  "https://www.congress.gov/109/crec/2005/02/15/CREC-2005-02-15-pt1-PgE247.pdf": "neutral",
  "https://assets.nfhs.org/umbraco/media/1019429/treaties.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Gardiner says Langevin opposed U.S.-Mexican border fence for fear someone will get hurt**
   URL: https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/
   Stance: `supporting`

2. **PolitiFact**
   URL: https://www.politifact.com/search/factcheck/?q=Trang%20ch%E1%BB%A7%20D%E1%BA%ABn%20l%C6%B0u%20m%C3%A0n%20h%C3%ACnh%20b%C3%A1%20ch%E1%BB%A7%28TG%3Ae10838%29.frm
   Stance: `neutral`

3. **James Langevin on Immigration**
   URL: https://www.ontheissues.org/house/James_Langevin_Immigration.htm
   Stance: `neutral`

4. **CONSTRUCTION OPTIONS AND STRATEGIC PLACEMENT**
   URL: https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm
   Stance: `neutral`

5. **THE WAY FORWARD ON BORDER SECURITY**
   URL: https://www.congress.gov/event/116th-congress/house-event/LC64036/text
   Stance: `neutral`

6. **PolitiFact | Fact-check: Did top Democrats vote for a border wall in 2006?**
   URL: https://www.politifact.com/factchecks/2017/apr/23/mick-mulvaney/fact-check-did-top-democrats-vote-border-wall-2006/
   Stance: `neutral`

7. **[PDF] CONGRESSIONAL RECORD— Extensions of ... - Congress.gov**
   URL: https://www.congress.gov/109/crec/2005/02/15/CREC-2005-02-15-pt1-PgE247.pdf
   Stance: `neutral`

8. **[PDF] International Treaties**
   URL: https://assets.nfhs.org/umbraco/media/1019429/treaties.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 23. PolitiFact / pf_022 - mostly-true

#### Input
- **Claim:** Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `mostly_true, true`
- **TLDR:** Sources don’t substantiate the specific 100 layoffs or the CEO’s $500k Kasich-PAC check.
- **Explanation:** Source 6 (PolitiFact) addresses the exact combined statement and rates it “mostly-true,” but the provided excerpt does not include the underlying evidence for the “laid off 100 Ohioans” or the “half-million-dollar check” details. Sources 1, 2, 4 discuss broad patterns of Ohio job-creation tax credits failing to meet promises, and Source 3 describes a different company (TimberTech) cutting 58 jobs after a tax credit—none of which corroborate the specific “100 Ohioans” or the CEO’s $500,000 check to Kasich’s super PAC. Therefore, the specific factual elements of the claim are not supported by the provided source excerpts.
- **Confidence reason:** Only one source directly mentions the claim; excerpts lack key supporting details.
- **Claim verdicts:**
```json
[
  {
    "claim": "A company that got tax breaks from the state later laid off 100 Ohioans.",
    "verdict": "unverifiable"
  },
  {
    "claim": "The company's CEO cut a half-million-dollar check to Kasich's super PAC.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://signalohio.org/most-job-creation-tax-credits-failed-to-create-ohio-jobs-as-promised-audit-says/": "neutral",
  "https://www.dispatch.com/story/business/employment/2025/12/04/ohio-business-loans-tax-breaks-jobs-report/87605321007/": "neutral",
  "https://www.bricker.com/DevelopOhio/After-receiving-a-tax-credit-to-create-85-new-jobs-in-Wilmington-TimberTech-eliminates-58-jobs-with-the-closing-of-its-Columbus-factory": "neutral",
  "https://www.statenews.org/government-politics/2026-01-13/nearly-two-thirds-of-companies-that-got-incentives-from-ohio-didnt-deliver-on-jobs-pay": "neutral",
  "https://ohiocapitaljournal.com/2025/12/03/hardworking-ohio-auto-workers-are-paying-the-price-for-ev-tax-credit-rollback/": "neutral",
  "https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/": "supporting",
  "https://www.politifact.com/factchecks/list/?target=john-kasich": "neutral",
  "https://www.factcheck.org/2016/01/new-day-for-america/": "neutral"
}
```

#### Pipeline Sources Output
1. **State tax credits failed to create promised Ohio jobs, audit says**
   URL: https://signalohio.org/most-job-creation-tax-credits-failed-to-create-ohio-jobs-as-promised-audit-says/
   Stance: `neutral`

2. **Ohio gave business loans, tax breaks to create jobs. 65% didn't comply**
   URL: https://www.dispatch.com/story/business/employment/2025/12/04/ohio-business-loans-tax-breaks-jobs-report/87605321007/
   Stance: `neutral`

3. **After receiving a tax credit to create 85 new jobs in Wilmington, TimberTech eliminates 58 jobs with the closing of its Columbus factory**
   URL: https://www.bricker.com/DevelopOhio/After-receiving-a-tax-credit-to-create-85-new-jobs-in-Wilmington-TimberTech-eliminates-58-jobs-with-the-closing-of-its-Columbus-factory
   Stance: `neutral`

4. **Nearly two-thirds of companies that got incentives from Ohio didn't deliver on jobs, pay | The Statehouse News Bureau**
   URL: https://www.statenews.org/government-politics/2026-01-13/nearly-two-thirds-of-companies-that-got-incentives-from-ohio-didnt-deliver-on-jobs-pay
   Stance: `neutral`

5. **Hardworking Ohio auto workers are paying the price for EV tax credit rollback • Ohio Capital Journal**
   URL: https://ohiocapitaljournal.com/2025/12/03/hardworking-ohio-auto-workers-are-paying-the-price-for-ev-tax-credit-rollback/
   Stance: `neutral`

6. **PolitiFact | Ted Cruz ad revisits a controversy from Kasich’s governorship of Ohio**
   URL: https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/
   Stance: `supporting`

7. **Fact-checks | PolitiFact**
   URL: https://www.politifact.com/factchecks/list/?target=john-kasich
   Stance: `neutral`

8. **New Day for America - FactCheck.org**
   URL: https://www.factcheck.org/2016/01/new-day-for-america/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 24. PolitiFact / pf_025 - mostly-true

#### Input
- **Claim:** Federal spending on entitlements is projected to consume all revenue by 2045.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `20`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `mostly_true, true`
- **TLDR:** CBO-based analysis in the sources says entitlements would not consume all federal revenue by 2045.
- **Explanation:** Source 1 directly evaluates the specific claim and concludes that using CBO’s current-law projections, entitlements would not consume every revenue dollar by 2045 (though they would take a larger share). Source 2 discusses entitlement spending rising and crowding out other spending, but it does not state that entitlements consume all revenue by 2045. Therefore, the provided sources mostly contradict the claim as stated.
- **Confidence reason:** Only one source directly addresses the 2045 “all revenue” wording.
- **Claim verdicts:**
```json
[
  {
    "claim": "Federal spending on entitlements is projected to consume all revenue by 2045.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/": "contradicting",
  "https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html": "neutral",
  "https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf": "neutral",
  "https://www.crfb.org/papers/explaining-federal-spending-and-revenue": "neutral",
  "https://budgetmodel.wharton.upenn.edu/t/Entitlements/": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Ohio Treasurer Josh Mandel says entitlement spending expected to consume all federal revenue by 2045**
   URL: https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/
   Stance: `contradicting`

2. **Fiscal Challenges: Health Care, Taxes and Beyond**
   URL: https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html
   Stance: `neutral`

3. **[PDF] Demographic Headwinds - Aspen Economic Strategy Group**
   URL: https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf
   Stance: `neutral`

4. **Explaining Federal Spending and Revenue-Wed, 05/21/2025 - 12:00 | Committee for a Responsible Federal Budget**
   URL: https://www.crfb.org/papers/explaining-federal-spending-and-revenue
   Stance: `neutral`

5. **Entitlements | Penn Wharton Budget Model**
   URL: https://budgetmodel.wharton.upenn.edu/t/Entitlements/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 25. PolitiFact / pf_030 - true

#### Input
- **Claim:** Today California is kicking our butt, creating more jobs and more economic growth than Texas.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact’s cited data supports California outpacing Texas on jobs and growth.
- **Explanation:** Source 1 (PolitiFact) explicitly evaluates the June 2016 claim and rates it True, citing higher California job growth (3% vs Texas 1.5%) and other economic indicators. Source 2 (PolitiFact) also reports Castro’s “kicking our butt” statement and includes supporting metrics like higher GDP growth for California than Texas over the cited period. Other provided sources (3-5) discuss later or different comparisons and do not directly address the specific “today” 2016 claim, so they don’t meaningfully contradict the PolitiFact findings.
- **Confidence reason:** Only PolitiFact directly addresses the exact 2016 “today” claims.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today California is creating more jobs and more economic growth than Texas.",
    "verdict": "supported"
  },
  {
    "claim": "Today California is kicking our butt.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/": "supporting",
  "https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/": "supporting",
  "https://businessintexas.com/blog/texas-vs-california-economy-which-state-is-best-for-business/": "neutral",
  "https://statspanda.com/blog/texas-vs-california-comparison": "neutral",
  "https://www.linkedin.com/posts/txedc_when-you-look-at-the-data-one-thing-becomes-activity-7424100550503493632-jZS0": "neutral",
  "https://www.usatoday.com/story/news/factcheck/2020/10/02/fact-check-clint-eastwood-did-not-author-pro-trumps-post/5885225002/": "neutral",
  "https://www.factcheck.org/": "neutral",
  "https://www.instagram.com/p/DTElWYDCQVS/": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Is California's economy 'growing a hell of a lot faster' than Texas?**
   URL: https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/
   Stance: `supporting`

2. **PolitiFact | Julián Castro says California besting Texas in creating jobs, economic growth**
   URL: https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/
   Stance: `supporting`

3. **Texas vs. California Economy: Which State is Best for Business? | TxEDC**
   URL: https://businessintexas.com/blog/texas-vs-california-economy-which-state-is-best-for-business/
   Stance: `neutral`

4. **Texas vs California: America's Two Largest State Economies Compared by the Data | StatsPanda Blog | StatsPanda**
   URL: https://statspanda.com/blog/texas-vs-california-comparison
   Stance: `neutral`

5. **Texas Outpaces California in Job Growth and Unemployment Rate | Texas Economic Development Corporation posted on the topic | LinkedIn**
   URL: https://www.linkedin.com/posts/txedc_when-you-look-at-the-data-one-thing-becomes-activity-7424100550503493632-jZS0
   Stance: `neutral`

6. **Fact check: Clint Eastwood did not author pro-Trump social media post**
   URL: https://www.usatoday.com/story/news/factcheck/2020/10/02/fact-check-clint-eastwood-did-not-author-pro-trumps-post/5885225002/
   Stance: `neutral`

7. **FactCheck.org - A Project of The Annenberg Public Policy Center**
   URL: https://www.factcheck.org/
   Stance: `neutral`

8. **Instagram**
   URL: https://www.instagram.com/p/DTElWYDCQVS/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:
