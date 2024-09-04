import arxiv


def fetch_papers():
    search = arxiv.Search(
        query="cat:cs.AI|cs.CV|cs.CL|cs.SD",
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    client = arxiv.Client()
    return [result.pdf_url for result in client.results(search)]


def main():
    papers = fetch_papers()


if __name__ == "__main__":
    main()
