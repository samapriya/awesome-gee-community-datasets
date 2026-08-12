# Catalog Assistant

The **Catalog Assistant** is a custom-designed assistant for the Community Catalog, available at [search.gee-community-catalog.org](https://search.gee-community-catalog.org). Ask it questions in plain language and it returns summaries **grounded** in the catalog's own pages and dataset metadata — with links back to the source material, so you can verify every answer. You can still use the embedded search within the Community Catalog for basic keyword or text-match lookups.

[Open the Catalog Assistant here.](https://search.gee-community-catalog.org)

<div class="result" markdown>

???+ note

    **If the assistant doesn't work as expected, try disabling any widget blocker extensions or using an incognito window to troubleshoot.**

</div>

![catalog_search](https://github.com/user-attachments/assets/52393c93-ed42-4d2e-ba02-43b7738ea51b)

## Salient Features

- Answers are **grounded** in the catalog — every summary links back to the source pages and dataset metadata, boosting trust and minimizing inaccuracies.
- Supports **multiple languages** — ask in your preferred language and the results are summarized in the same language.
- As with all generative assistants, **prompt formulation** matters. Slight changes in phrasing can often yield better results.

## Limitations

- Summaries are generated from a limited set of top results, so not every matching dataset may appear in a given answer.
- Summaries may evolve over time as the **context window** changes, so your answer might vary between searches.

## Previous deployment

Earlier versions of the assistant ran as a **Vertex AI** search widget built on **RAG (Retrieval Augmented Generation)**, drawing on two data stores — the Community Catalog pages and a JSON data store — to keep its summaries grounded in reliable sources. That deployment was offered in **Beta** while we tested and refined it, and its output was a server-side–controlled widget that generated summaries from up to ten search results. Learn more about RAG in [this earlier blog post](https://datacommons.substack.com/p/can-ai-turn-slides-into-podcasts). Notable changes from that phase:

- Added a secondary data store (JSON) to speed up parsing of details like licenses and links.
- Introduced a "Back to the Community Catalog" button for easy navigation back to the main catalog.
- Implemented custom system instructions to improve output quality and relevance.
