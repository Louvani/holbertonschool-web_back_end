#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end indexes
    """
    return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        that takes two integer arguments page with default value 1 and
        page_size with default value 10.

        You have to use this CSV file (same as the one presented at the
        top of the project)
        Use assert to verify that both arguments are integers greater than 0.
        Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset (i.e. the
        correct list of rows).
        If the input arguments are out of range for the dataset, an empty
        list should be returned.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return pagination information
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': page_size if page < total_pages else 0,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
