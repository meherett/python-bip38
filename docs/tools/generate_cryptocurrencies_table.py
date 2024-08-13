#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse Yae <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import inspect

from bip38 import cryptocurrencies

# Create a dictionary of cryptocurrency classes in the BIP38 module
BIP38_CRYPTOCURRENCIES: dict = {
    name: cls for name, cls in inspect.getmembers(cryptocurrencies, inspect.isclass)
    if issubclass(cls, cryptocurrencies.ICryptocurrency)
}

del BIP38_CRYPTOCURRENCIES["ICryptocurrency"]

# Table headers
markdown_table: str = (
    "<table><thead><tr><th align='left'>Name</th><th>Network</th>"
    "<th>WIF Prefix</th><th>Address Prefix</th></tr></thead><tbody>"
)

rst_table: str = (
    "<div class='table-wrapper doctils container'><table class='docutils align-default'>"
    "<thead><tr class='row-odd'><th class='head name'><p>Name</p></th>"
    "<th class='head'><p>Network</p></th><th class='head'><p>WIF Prefix</p></th>"
    "<th class='head'><p>Address Prefix</p></th></tr></thead><tbody>"
)

# Iterate over the sorted list of cryptocurrency names.
for crypto in sorted(BIP38_CRYPTOCURRENCIES.keys()):
    # Get the number of networks.
    network_count: int = len(BIP38_CRYPTOCURRENCIES[crypto].NETWORKS.keys())

    # Iterate over the networks of the current cryptocurrency.
    for idx, net in enumerate(BIP38_CRYPTOCURRENCIES[crypto].NETWORKS):
        # Get the prefix values for WIF and address for the current network.
        prefixes = BIP38_CRYPTOCURRENCIES[crypto].NETWORKS[net]

        # Add the cryptocurrency name only for the first network in the row.
        if not idx:
            markdown_table += (
                f"<tr><td align='left' rowspan='{network_count}'>{crypto}</td>"
            )
            rst_table += (
                f"<tr class='row-even'><td class='name' rowspan='{network_count}'><p>{crypto}</p></td>"
            )
        else:
            markdown_table += "<tr>"
            rst_table += "<tr class='row-even'>"

        # Add the network name, WIF prefix, and address prefix to the Markdown table.
        markdown_table += (
            f"<td align='center'><code>{net}</code></td>"
            f"<td align='center'><code>0x{prefixes['wif_prefix']:02x}</code></td>"
            f"<td align='center'><code>0x{prefixes['address_prefix']:02x}</code></td></tr>"
        )

        # Add the network name, WIF prefix, and address prefix to the reStructuredText table.
        rst_table += (
            f"<td><p><code class='xref py py-class docutils literal notranslate'>"
            f"<span class='pre'>{net}</span></code></p></td>"
            f"<td><p><code class='xref py py-class docutils literal notranslate'>"
            f"<span class='pre'>0x{prefixes['wif_prefix']:02x}</span></code></p></td>"
            f"<td><p><code class='xref py py-class docutils literal notranslate'>"
            f"<span class='pre'>0x{prefixes['address_prefix']:02x}</span></code></p></td></tr>"
        )

markdown_table += "</tbody></table>"
rst_table += "</tbody></table></div>"

with open("output.md", "w") as md_file:
    md_file.write(markdown_table)

with open("output.rst", "w") as rst_file:
    rst_file.write(rst_table)
