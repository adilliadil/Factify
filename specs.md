# TruthLens -- MVP Technical Specification

AI-powered Chrome extension for verifying factual claims on webpages.

------------------------------------------------------------------------

## 1. Overview

TruthLens is a Chrome extension that fact-checks claims on webpages.

Users highlight text on a webpage and run **"Check Claim"**.

The extension sends the text to a backend which:

1.  Extracts factual claims
2.  Searches the web for relevant sources
3.  Compares sources against the claim
4.  Computes a truthfulness score
5.  Returns a summary and supporting links

The result is displayed in the extension popup.

------------------------------------------------------------------------

## 2. MVP Goals

The MVP must:

-   Work on highlighted text
-   Extract factual claims
-   Retrieve external sources
-   Evaluate support vs contradiction
-   Produce a truth score (0--100)
-   Show explanation and source links

The MVP does NOT attempt full automated article verification.

------------------------------------------------------------------------

## 3. User Flow

### Step 1

User highlights text on a webpage.

Example:

    Vitamin C cures the flu in 24 hours.

### Step 2

User right-clicks and selects:

    Check Claim

### Step 3

Extension sends request to backend.

Endpoint:

    POST /factcheck

Payload:

``` json
{
  "text": "Vitamin C cures the flu in 24 hours."
}
```

### Step 4

Backend performs fact-check pipeline.

### Step 5

Extension shows result popup.

Example:

Claim: Vitamin C cures the flu in 24 hours\
Truth Score: 18 / 100

Assessment: Claim contradicts medical consensus.

Evidence: - CDC: No cure exists for flu - Mayo Clinic: Vitamin C does
not cure influenza

------------------------------------------------------------------------

## 4. System Architecture

    Chrome Extension
            |
            v
    Backend API (FastAPI)
            |
            v
    Fact Check Pipeline
       |        |
       v        v
    Search API  LLM

------------------------------------------------------------------------

## 5. Tech Stack

### Frontend

Chrome Extension

-   Manifest V3
-   React
-   Chrome contextMenus API

### Backend

Python

Recommended stack:

-   FastAPI
-   httpx
-   BeautifulSoup
-   Pydantic

### LLM

Recommended model:

    gpt-5-mini

### Search API

Recommended for MVP: Tavily

------------------------------------------------------------------------

## 6. Backend API

### POST /factcheck

Request:

``` json
{
  "text": "Vitamin C cures the flu in 24 hours"
}
```

Response:

``` json
{
  "claims": [
    "Vitamin C cures the flu in 24 hours"
  ],
  "score": 18,
  "verdict": "mostly_false",
  "explanation": "Medical authorities state that vitamin C does not cure influenza.",
  "sources": [
    {
      "title": "CDC Flu Treatment",
      "url": "https://cdc.gov/..."
    },
    {
      "title": "Mayo Clinic Flu Treatment",
      "url": "https://mayoclinic.org/..."
    }
  ]
}
```

------------------------------------------------------------------------

## 7. Fact Check Pipeline

### Step 1 -- Claim Extraction

Prompt:

    Extract factual claims from the text.
    Return JSON array.
    Ignore opinions and predictions.

    Text:
    {input_text}

Example output:

``` json
[
  "Vitamin C cures the flu in 24 hours"
]
```

------------------------------------------------------------------------

### Step 2 -- Web Search

Query format:

    {claim} evidence

Retrieve top 5 results.

Fields:

-   title
-   url
-   snippet

------------------------------------------------------------------------

### Step 3 -- Source Retrieval

For each result:

1.  Download page HTML
2.  Extract readable text using BeautifulSoup

Limit extracted text to **2000 characters**.

------------------------------------------------------------------------

### Step 4 -- Evidence Analysis

Prompt:

    You are a fact-checking assistant.

    Evaluate whether the provided sources support or contradict the claim.

    Claim:
    {claim}

    Sources:
    {source_texts}

    Return JSON:

    {
      "score": 0-100,
      "verdict": "false | mostly_false | mixed | mostly_true | true | unverifiable",
      "explanation": "..."
    }

    Do not invent sources.
    Only use the provided information.

------------------------------------------------------------------------

### Step 5 -- Score Mapping

  Score     Meaning
  --------- --------------
  0--20     False
  21--40    Mostly False
  41--60    Mixed
  61--80    Mostly True
  81--100   True

------------------------------------------------------------------------

## 8. Chrome Extension Design

### File Structure

    extension/
      manifest.json
      background.js
      content.js
      popup.html
      popup.js
      styles.css

### manifest.json Permissions

-   contextMenus
-   activeTab
-   scripting
-   storage

### Context Menu Example

``` javascript
chrome.contextMenus.create({
  title: "Check Claim",
  contexts: ["selection"],
  id: "check_claim"
});
```

Popup should display:

-   Claim
-   Truth Score
-   Verdict
-   Explanation
-   Source links

------------------------------------------------------------------------

## 9. Error Handling

Cases to handle:

No claim detected → "No factual claims detected."

Unverifiable claims example:

    AI will replace programmers.

Return verdict:

    unverifiable

Search failure → "Unable to retrieve sources."



## 10. MVP Acceptance Criteria

The MVP is complete when:

-   User highlights text on a webpage
-   Extension sends text to backend
-   Backend retrieves sources
-   System produces a truth score
-   Extension displays result with explanation and sources
