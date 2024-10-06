# Advanced Search for Awesome GEE Community Catalog

The **Advanced Search** feature of the Community Catalog leverages **Vertex AI** to enhance documentation search. This search is powered by both the catalog pages and **Data JSON** tabular structures. As more people use the feature, the indexed results improve over time. The feature benefits from **grounded search**, meaning that its summaries are always linked to the source material, ensuring transparency and trustworthiness.

This is made possible by **RAG (Retrieval Augmented Generation)**, which not only improves search relevancy but also minimizes misinformation by grounding the output in reliable sources. Learn more about RAGs [here in an earlier blog post](https://datacommons.substack.com/p/can-ai-turn-slides-into-podcasts) to understand why this is so powerful and why grounded search can be effective. Currently, this search is in **Beta**, allowing us to test and refine it further with your participation. You can still use the embedded search within the Community Catalog for basic keyword or text-match searches.

[Find the Advanced Search here.](https://gee-community-catalog.org/search)

<div class="result" markdown>

???+ note

    **If the search doesn't work as expected, try disabling any widget blocker extensions or using an incognito window to troubleshoot.**

</div>

![catalog_search](https://github.com/user-attachments/assets/52393c93-ed42-4d2e-ba02-43b7738ea51b)

## Salient Features

- Utilizes two data stores: the Community Catalog itself and the JSON data store. This dual approach enables quicker and more effective parsing across the data.
- The search widget supports **multiple languages**. You can ask questions in your preferred language, and the results will be summarized in the same language.
- As with all generative AI search engines, **prompt formulation** matters. Slight changes in phrasing can often yield better results.
- Built on **RAG (Retrieval Augmented Generation)** technology, meaning summaries come with links to the source material. This boosts trust and minimizes inaccuracies.

## Limitations

- The final summary is generated from up to **10 search results**. If multiple results meet the same criteria, not all may be included in the summary.
- Summaries may evolve over time as the **context window** changes. Therefore, your summary might vary with each search.
- Current output is part of a server-side controlled widget, which may affect customization or fine-tuning on the user end.

## Changelog

- Added a secondary data store (JSON) to speed up parsing of details like licenses and links.
- Introduced a "Back to the Community Catalog" button for easy navigation back to the main catalog.
- Implemented custom system instructions to improve output quality and relevance.
