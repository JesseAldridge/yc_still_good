const all_valuations = [
  {
    name: 'Airbnb',
    valuations: [
      {billions: 0, year: 2008}, // https://www.crunchbase.com/organization/airbnb#section-overview
      {billions: 1, year: 2011}, // https://techcrunch.com/2011/05/30/airbnb-has-arrived-raising-mega-round-at-a-1-billion-valuation/
      {billions: 2.5, year: 2012}, // https://www.forbes.com/sites/calebmelby/2012/10/19/peter-thiel-may-invest-150-million-in-airbnb-at-2-5-billion-valuation/#47ea6d6a5434
      {billions: 10, year: 2014}, // https://techcrunch.com/2014/04/18/airbnb-has-closed-its-500m-round-of-funding-at-a-10b-valuation-led-by-tpg/
      {billions: 24, year: 2015}, // http://fortune.com/2015/06/17/airbnb-valuation-revenue/
      {billions: 31, year: 2017}, // https://www.forbes.com/sites/greatspeculations/2018/05/11/as-a-rare-profitable-unicorn-airbnb-appears-to-be-worth-at-least-38-billion/#4f5c3b92741e
      {billions: 38, year: 2018} // https://www.forbes.com/sites/greatspeculations/2018/05/11/as-a-rare-profitable-unicorn-airbnb-appears-to-be-worth-at-least-38-billion/#4f5c3b92741e
    ]
  },
  {
    name: 'Cruise',
    valuations: [
      {billions: 0, year: 2013}, // https://www.crunchbase.com/organization/cruise#section-overview
      {billions: 1, year: 2016}, // https://www.investors.com/news/gm-softbank-investment-cruise-self-driving-cars/
      {billions: 11.5, year: 2018}, // https://www.investors.com/news/gm-softbank-investment-cruise-self-driving-cars/
    ],
  },
  {
    name: 'DoorDash',
    valuations: [
      {billions: 0, year: 2013}, // https://www.crunchbase.com/organization/doordash
      {billions: 4, year: 2018}, // https://techcrunch.com/2018/08/16/doordash-4-billion/
    ]
  },
  {
    name: 'Dropbox',
    valuations: [
      {billions: 0, year: 2007}, // https://www.crunchbase.com/organization/dropbox
      {billions: .029, year: 2008}, // https://www.quora.com/At-what-valuation-did-Dropbox-raise-its-7-million-round-from-Sequoia
      {billions: 4, year: 2011}, // https://techcrunch.com/2011/08/30/index-leads-4-billion-valuation-round-in-dropbox/
      {billions: 8, year: 2013}, // https://www.thedailybeast.com/is-dropbox-worth-dollar8-billion
      {billions: 10, year: 2014}, // https://www.cbinsights.com/research/dropbox-valuation-bubble/
      {billions: 10.79, year: 2018}, // https://www.google.com/search?q=dropbox+market+cap&oq=dropbox+market+cap
    ]
  },
  {
    name: 'Flexport',
    valuations: [
      {billions: 0, year: 2013}, // https://www.crunchbase.com/organization/flexport
      {billions: .365, year: 2016}, // https://techcrunch.com/2017/09/21/container-full-of-cash/
      {billions: .8, year: 2017} // https://techcrunch.com/2017/09/21/container-full-of-cash/
    ]
  },
  {
    name: 'Instacart',
    valuations: [
      {billions: 0, year: 2012}, // https://www.crunchbase.com/organization/instacart
      {billions: 3.4, year: 2017}, // https://techcrunch.com/2017/03/07/instacart-raises-400-million-at-a-3-4-billion-valuation-to-deliver-groceries-on-demand/
      {billions: 4.2, year: 2018}, // https://techcrunch.com/2018/02/12/instacart-has-raised-another-200m-at-a-4-2b-valuation/
    ]
  },
  {
    name: 'PlanGrid',
    valuations: [
      {billions: 0, year: 2011}, // https://www.crunchbase.com/organization/plangrid
    ],
  },
  {
    name: 'Docker',
    valuations: [
      {billions: 0, year: 2010},  // https://www.crunchbase.com/organization/docker
      {billions: 1.3, year: 2017}, // https://www.bloomberg.com/news/articles/2017-08-09/docker-is-said-to-be-raising-funding-at-1-3-billion-valuation
    ]
  },
  {
    name: 'Segment',
    valuations: [
      {billions: 0, year: 2011}, // https://www.crunchbase.com/organization/segment-io
    ],
  },
  {
    name: 'Stripe',
    valuations: [
      {billions: 0, year: 2010}, // https://www.crunchbase.com/organization/stripe
      {billions: .5, year: 2012}, // https://techcrunch.com/2012/07/09/payments-startup-stripe-swipes-20m-from-general-catalyst-sequoia-thiel-and-more/
      {billions: 3.5, year: 2014}, // https://techcrunch.com/2014/12/02/stripe-3-5-billion/
      {billions: 9, year: 2016}, // http://fortune.com/2016/11/25/payments-stripe-valuation/
      {billions: 20, year: 2018}, // http://fortune.com/2018/09/27/stripe-valuation-ipo-stock/
    ]
  },
  {
    name: 'Twitch',
    valuations: [
      {billions: 0, year: 2007}, // https://www.crunchbase.com/organization/twitch
      {billions: .97, year: 2014} // https://en.wikipedia.org/wiki/Twitch.tv
    ]
  },
  {
    name: 'Mixpanel',
    valuations: [
      {billions: 0, year: 2009}, // https://www.crunchbase.com/organization/mixpanel
      {billions: .865, year: 2014} // https://www.quora.com/What-is-the-most-recent-valuation-of-MixPanel
    ]
  },
  {
    name: 'Gusto',
    valuations: [
      {billions: 0, year: 2011}, // https://www.crunchbase.com/organization/gusto
      {billions: 2, year: 2018}, // https://www.bloomberg.com/news/articles/2018-07-31/payroll-startup-gusto-raises-140-million-in-funding
    ]
  },
  {
    name: 'Reddit',
    valuations: [
      {billions: 0, year: 2005}, // https://www.crunchbase.com/organization/reddit
      {billions: 1.8, year: 2017}, // https://www.recode.net/2017/7/31/16037126/reddit-funding-200-million-valuation-steve-huffman-alexis-ohanian
    ]
  },
  {
    name: 'Coinbase',
    valuations: [
      {billions: 0, year: 2012}, // https://www.crunchbase.com/organization/coinbase
      {billions: 1.6, year: 2017}, // https://news.bitcoin.com/coinbase-valuation-jumps-from-1-6-billion-to-as-high-as-8-billion/
      {billions: 8, year: 2018}, // https://www.recode.net/2018/4/27/17287184/coinbase-earn-acquisition-stock-valuation-eight-billion-earn
    ]
  },
  {
    name: 'Weebly',
    valuations: [
      {billions: 0, year: 2007}, // https://www.crunchbase.com/organization/weebly
      {billions: .49, year: 2015}, // https://news.crunchbase.com/news/square-acquires-website-builder-weebly/
      {billions: .365, year: 2018}, // https://news.crunchbase.com/news/square-acquires-website-builder-weebly/
    ]
  },
  {
    name: 'Ginkgo Bioworks',
    valuations: [
      {billions: 0, year: 2009},
      {billions: 1, year: 2017},
    ]
  },
  {
    name: 'Gitlab',
    valuations: [
      {billions: 0, year: 2014}, // https://www.crunchbase.com/organization/gitlab
      {billions: 1.1, year: 2018}, // https://techcrunch.com/2018/09/19/gitlab-raises-100m/
    ]
  },
  {
    name: 'Rappi',
    valuations: [
      {billions: 0, year: 2015}, // https://www.crunchbase.com/organization/rappi
      {billions: 1, year: 2018}, // https://techcrunch.com/2018/08/31/rappi-raises-200m-as-latin-american-tech-investment-reaches-new-highs/
    ]
  },
  {
    name: 'Zenefits',
    valuations: [
      {billions: 0, year: 2013}, // https://www.crunchbase.com/organization/zenefits
      {billions: 4.5, year: 2015}, // https://techcrunch.com/2015/05/06/zenefits-rising-hrs-hottest-startup-just-raised-500-million-at-a-4-5-billion-valuation/
      {billions: 2, year: 2016}, // https://www.nytimes.com/2016/07/01/technology/zenefits-compensates-investors-over-past-misconduct.html
    ]
  },
];
