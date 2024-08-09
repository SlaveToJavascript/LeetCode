# 1236. Web Crawler
# https://leetcode.com/problems/web-crawler/
# MEDIUM
# Tags: dfslc, bfslc, premiumlc, #1236

# Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl. 
# Return all urls obtained by your web crawler in any order.
# Your crawler should:
    # Start from the page: startUrl
    # Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
    # Do not crawl the same link twice.
    # Explore only the links that are under the same hostname as startUrl.
# As shown in the example url above, the hostname is example.org. For simplicity sake, you may assume all urls use http protocol without any port specified. For example, the urls http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, while urls http://example.org/test and http://example.com/abc are not under the same hostname.

# The HtmlParser interface is defined as such: 
# interface HtmlParser {
#   # Return a list of all urls from a webpage of given url.
#   public List<String> getUrls(String url);
# }
# Below are two examples explaining the functionality of the problem, for custom testing purposes you'll have three variables urls, edges and startUrl. Notice that you will only have access to startUrl in your code, while urls and edges are not directly accessible to you in code.

# Note: Consider the same URL with the trailing slash "/" as a different URL. For example, "http://news.yahoo.com", and "http://news.yahoo.com/" are different urls.

# EXAMPLES:
    # Input:
    # urls = [
    #   "http://news.yahoo.com",
    #   "http://news.yahoo.com/news",
    #   "http://news.yahoo.com/news/topics/",
    #   "http://news.google.com",
    #   "http://news.yahoo.com/us"
    # ]
    # edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
    # startUrl = "http://news.yahoo.com/news/topics/"
    # Output: [
    #   "http://news.yahoo.com",
    #   "http://news.yahoo.com/news",
    #   "http://news.yahoo.com/news/topics/",
    #   "http://news.yahoo.com/us"
    # ]

    # Input: 
    # urls = [
    #   "http://news.yahoo.com",
    #   "http://news.yahoo.com/news",
    #   "http://news.yahoo.com/news/topics/",
    #   "http://news.google.com"
    # ]
    # edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
    # startUrl = "http://news.google.com"
    # Output: ["http://news.google.com"]
    # Explanation: The startUrl links to all other pages that do not share the same hostname.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS

# TIME COMPLEXITY: O(V+E)
    # V = no. of unique URLs that are under the same hostname as startUrl and reachable from startUrl
    # E = no. of edges (links) between these URLs
    # dfs() takes O(V+E) for node processing (visiting each node once) and edge processing (retrieving all neighbors (links) from htmlParser and checking if the hostnames match) respectively
# SPACE COMPLEXITY: O(V)
    # visited set takes O(V) space
    # recursive stack takes O(V) space

def crawl(startUrl, htmlParser):
    def get_hostname(url):
        return url.split('/')[2] # e.g. "http://host.org/foo" will be split into "http:", "", "host.org", "foo" -> hostname is the 2nd element (0-indexed)

    visited = set()
    def dfs(url):
        if url in visited:
            return
        visited.add(url)
        for neighbor in htmlParser.getUrls(url):
            if get_hostname(neighbor) == get_hostname(url):
                dfs(neighbor)
    
    dfs(startUrl)
    return list(visited)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE BFS

# TIME COMPLEXITY: O(V+E)
    # V = no. of unique URLs that are under the same hostname as startUrl and reachable from startUrl
    # E = no. of edges (links) between these URLs
    # dfs() takes O(V+E) for node processing (visiting each node once) and edge processing (retrieving all neighbors (links) from htmlParser and checking if the hostnames match) respectively
# SPACE COMPLEXITY: O(V)
    # visited set takes O(V) space
    # recursive stack takes O(V) space

from collections import deque

def crawl(startUrl, htmlParser):
    def get_hostname(url):
        return url.split('/')[2] # e.g. "http://host.org/foo" will be split into "http:", "", "host.org", "foo" -> hostname is the 2nd element (0-indexed)
    
    q = deque([startUrl])
    visited = set()
    while q:
        url = q.popleft()
        if url in visited:
            continue
        visited.add(url)
        for neighbor in htmlParser.getUrls(url):
            if get_hostname(neighbor) == get_hostname(url):
                q.append(neighbor)
    
    return list(visited)