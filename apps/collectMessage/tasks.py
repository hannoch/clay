from __future__ import absolute_import
from celery import shared_task

from worker.dnsmaper.dnsmaper import *


@shared_task(track_started=True)
def dnsmaper(url):
    
    dns_zone_transfer_check(url)
    hosts = "./db/subs.db".split("\n")
    print('\n[!]Check DNS Resolvers..')
    resolve_list = check_resolvers("./db/resolvers.db")
    threads = []
    run_target(url, hosts, resolve_list, 17)
    print("[*]All Done.")


