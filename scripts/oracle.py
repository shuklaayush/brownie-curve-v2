#!/usr/bin/env python3
from brownie import accounts, chain, interface, web3, Contract, Trader

TREASURY = "0xd0a7a8b98957b9cd3cfb9c0425abe44551158e9e"
AMOUNT = web3.toWei(1_000_000, "ether")
SLEEP_MINS = 30


def main():
    accounts.default = accounts[0]

    trader = Trader.deploy()

    pool = interface.ICurveV2(trader.POOL())
    badger = interface.IERC20(trader.BADGER())
    wbtc = interface.IERC20(trader.WBTC())

    badger.transfer(trader, AMOUNT, {"from": TREASURY})

    print("-" * 80)
    print("Initially...")
    print(f"Price oracle: {pool.price_oracle() / 1e18}")
    print(f"Last price: {pool.last_prices() / 1e18}")
    print(f"Badger balance: {pool.balances(0) / 10**badger.decimals()}")
    print(f"Wbtc balance: {pool.balances(1) / 10**wbtc.decimals()}")
    print("-" * 80)

    trader.trade()

    print("-" * 80)
    print("After trades...")
    print(f"Price oracle: {pool.price_oracle() / 1e18}")
    print(f"Last price: {pool.last_prices() / 1e18}")
    print(f"Badger balance: {pool.balances(0) / 10**badger.decimals()}")
    print(f"Wbtc balance: {pool.balances(1) / 10**wbtc.decimals()}")
    print("-" * 80)

    chain.sleep(60 * SLEEP_MINS)
    chain.mine()
    print("-" * 80)
    print(f"After {SLEEP_MINS}mins..")
    print(f"Price oracle: {pool.price_oracle() / 1e18}")
    print("-" * 80)

