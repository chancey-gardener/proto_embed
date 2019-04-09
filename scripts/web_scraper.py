# !usr/bin/python3
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib3
import httplib2
import pickle, sys, re
from web_scraping.url_config import legal_webpages_by_organization, procedures_by_web_source
from os import mkdir
from os.path import exists

# TODO: make a version for the comprehensive code of the law (not just new bills introduced)
# this can be found at the same website..
#database = MySQLdb.connect()

# credit to jbochi for the tag_visible and text_from_html function
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


class LawScraper:

    def __init__(self, target_url, dat_dir, name=None, notes=None):
        self.dat_dir = dat_dir
        self.name = name
        self.data = {}
        self.http = httplib2.Http()


    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data[key]
        else:
            raise KeyError

    def get(self, year_range, from_states='all', org='justia', law_type='code'):
        # if the year is 
        generate_urls = procedures_by_web_source[org]
        self.urls = generate_urls(year_range=year_range, use_states=from_states)
        for url in urls:
            active_page = self.http.request('GET', url)
            soup = BeautifulSoup(active_page.data, 'html.parser')
            page_dat = soup.find_all(text=True)
            datstring = u' '.join(t.strip() for t in bill_dat)
            self.data[url] = datstring


def format_year_intervals(start, end, baseurl):
    '''generate a list of urls corresponding to year intervals'''

    # generate page names containing articles (This may want to be a function)
    pages = {}

    # TODO: write a regex that selects just the root url
    for date in range(start, end):
        begin, end = str(date), str(date+1)
        key = '{}-{}'.format(begin, end)
        url = baseurl.format(begin+end)
        pages[key] = url
    return pages





    def get_text(self, pages, outpath, root_url, ddir=dat_dir):
        '''given a dictionary with values corresponding to urls for bill indexes by year,
        return the text of each law introduced'''
        # Create a dictionary of soup objects and pickle them if specified in the command line to do so
        soup_ensemble = {}
        http = urllib3.PoolManager()
        all_texts = {}
        # create the contents of the year based directories
        for year_page in pages:
            print('getting laws from {}'.format(year_page))
            active_page = http.request('GET', pages[year_page])
            soup = BeautifulSoup(active_page.data, 'html.parser')
            # find all links on the current page.
            bill_pages = [link['href'] for link in soup.find_all('a', href=True) if 'bill_id' in link['href']]
            n_bills = len(bill_pages)
            print('links to the text of {} bills found\ndownloading and parsing html...'.format(n_bills))
            if outpath is not None:
                year_path = outpath+'/'+year_page
                if exists(outpath):
                    mkdir(year_path)
                else:
                    mkdir(outpath)
                    mkdir(year_path)
            # iterate over the webpages for each bill passed that year and get the text
            # TODO: get name of bills and use as keys/filenames. 
                #  TODO: figurre outwhy 2000-2001 is pulling 0 bills
                #  TODO: STREAM, get rid of all_texts, and write each text to file within get_text function
            for ind, bill in enumerate(bill_pages):
                bill_url = root_url+bill
                bill_page_dat = http.request('GET', bill_url).data
                bill_dat = filter(tag_visible, BeautifulSoup(bill_page_dat, 'html.parser').find_all(text=True))

                string_version = u' '.join(t.strip() for t in bill_dat)
                bkey = str(ind+1)
                textname = "{}_{}.txt".format(year_page, bill)

                all_texts[textname] = string_version
                if outpath is not None:
                    textpath = year_path+'/'+'bill{}'.format(bkey) # TODO: find place in text to get the actual names
                    # print('YEAR PATH: {}'.format(year_path))
                    # print('TEXT NAME: {}'.format(textname))
                    tfile = open(textpath, 'w')
                    tfile.write(string_version)
                    tfile.close()
                # print(string_version)
                # print('####################################################################################')
                barlen = 75
                done = int(barlen * ind / n_bills)
                sys.stdout.write("\r[%s%s]" % ('*' * done, ' ' * (barlen-done)) )    
                sys.stdout.flush()
            sys.stdout.write('\n')
                #\for test
            soup_ensemble[year_page] = soup
        # if not outpath is None:

        #     with open(outpath, 'w') as datfile:
        #         datfile.write(string_version)

        return soup_ensemble, all_texts



if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        dat_filename = sys.argv[1]
        outpath = dat_dir + dat_filename
        mkdir(outpath)

    else:
        outpath = None

    # test code from here down 

    # legal_webpages_by_organization = {'California': 'http://leginfo.legislature.ca.gov',
    #                                     'New_York': 'http://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO:',
    #                                     'Alabama': 'https://law.justia.com/codes/alabama/2017/'}
    all_laws = {}
    ca_law_url = 'http://leginfo.legislature.ca.gov/faces/billSearchClient.xhtml?session_year={}&house=Both&author=All&lawCode=All'
    ca_codes_url = 'https://leginfo.legislature.ca.gov/faces/codes.xhtml' # this is the base page to which are linked
    # initialize stable environment thus far                                # california constitution, education, housing codes, etc.
    page_dict = all_years(1999, 2017, ca_law_url)
    # what to do with all_dat? pickle and open in testing script to examine?
    # maybe just call get_text and have it write to file locally
    all_dat, textfiles = get_text(page_dict, root_url=ca_codes_url, outpath=outpath)
    # if outpath is not None:
    #     for name, text in textfiles.items():
    #         fname = outpath + name
    #         file = open(fname, 'w')
    #         file.write(text)
    #         file.close() # it already does?

    ########################################################################################################
    # Test code:

# dl = 0
# total_length = int(total_length)
# for data in response.iter_content(chunk_size=4096):
#     dl += len(data)
#     f.write(data)
#     done = int(50 * dl / total_length)
#     sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
#     sys.stdout.flush()


# download bar code


