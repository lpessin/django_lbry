from django.shortcuts import render
from . import sdk


# Home view. Trends
def home(request):
    trending = sdk.claim_search(28, claim_type='stream',
                                stream_types=['video'],
                                channel_ids=[],
                                order_by=['effective_amount'],
                                any_tags=['python', 'linux', 'economics', 'tutorial', 'art', 'apex legends', 'science'],
                                page_size=8)

    channels = sdk.claim_search(1000, claim_type='channel',
                                stream_types=[],
                                channel_ids=[],
                                order_by=['effective_amount'],
                                any_tags=['python', 'linux', 'economics', 'tutorial', 'art', 'apex legends', 'science'],
                                page_size=8)

    today = sdk.claim_search(1, claim_type='stream',
                             stream_types=['video'],
                             order_by=['effective_amount'],
                             channel_ids=[],
                             any_tags=['python', 'linux', 'economics', 'tutorial', 'art', 'apex legends', 'science'],
                             page_size=4)

    lbry = sdk.claim_search(claim_type='stream', channel_ids=['f8219d5914b95a0a2f670d92dea5dc24133278e9'],
                            order_by=['release_time'], page_size=4, page=1)

    context = {'trending': trending,
               'channels': channels,
               'today': today,
               'lbry': lbry}
    return render(request, 'pages/home.html', context)


# Search view. If the input is a lbry url renders either a channel or a stream page. Otherwise will render
# the search page with the search engine results
def search(request):
    search_input = request.GET.get('q', 'django lbry')
    search_url = search_input.replace(' ', '-')
    call = sdk.resolve(search_url)
    search = sdk.search_engine(search_input)
    if search_input.startswith('lbry://'):
        data = call
        if data.get('value_type') == 'channel':
            return render(request, 'pages/channel.html', data)
        else:
            return render(request, 'pages/stream.html', data)
    context = {'call': call,
               'search': search,
               'search_url': search_url}
    return render(request, 'pages/search.html', context)


# Resolve view. Renders a channel or a stream page.
def resolve(request, name, channel_name=None, claim_id=None):
    if channel_name:
        data = sdk.resolve(f'{channel_name}/{name}')
    elif claim_id:
        data = sdk.resolve(f'{name}#{claim_id}')
    else:
        data = sdk.resolve(f'{name}')
    if data.get('value_type') == 'channel':
        return render(request, 'pages/channel.html', data)
    else:
        return render(request, 'pages/stream.html', data)


# Under construction -- later some may belong to a second app -- some to be added
def wallet(request):
    return render(request, 'under_construction.html', {})


def publish(request):
    return render(request, 'under_construction.html', {})


def published(request):
    return render(request, 'under_construction.html', {})


def channels(request):
    return render(request, 'under_construction.html', {})


def dashboard(request):
    return render(request, 'under_construction.html', {})


def rewards(request):
    return render(request, 'under_construction.html', {})


def invite(request):
    return render(request, 'under_construction.html', {})


def settings(request):
    return render(request, 'under_construction.html', {})


def help(request):
    return render(request, 'under_construction.html', {})


def following(request):
    return render(request, 'under_construction.html', {})


def tags(request):
    return render(request, 'under_construction.html', {})


def discover(request):
    return render(request, 'under_construction.html', {})


def top(request):
    return render(request, 'under_construction.html', {})
