#!/usr/bin/env python3
from brownie import accounts, chain, interface, web3, Contract, Trader

POOL = "0x50f3752289e1456BfA505afd37B241bca23e685d"
BADGER = "0x3472A5A71965499acd81997a54BBA8D852C6E53d"
TREASURY = "0xd0a7a8b98957b9cd3cfb9c0425abe44551158e9e"

AMOUNT = web3.toWei(1_000_000, "ether")
SLEEP_MINS = 30


def main():
    accounts.default = accounts[0]

    trader = Trader.deploy(POOL)

    pool = interface.ICurveV2(POOL)
    token0 = interface.IERC20(trader.token0())
    token1 = interface.IERC20(trader.token1())

    token0.transfer(trader, AMOUNT, {"from": TREASURY})

    print("-" * 80)
    print("Initially...")
    print(f"Price oracle: {pool.price_oracle() / 1e18}")
    print(f"Last price: {pool.last_prices() / 1e18}")
    print(f"{token0.symbol()} balance: {pool.balances(0) / 10**token0.decimals()}")
    print(f"{token1.symbol()} balance: {pool.balances(1) / 10**token1.decimals()}")
    print("-" * 80)

    trader.trade()

    print("-" * 80)
    print("After trades...")
    print(f"Price oracle: {pool.price_oracle() / 1e18}")
    print(f"Last price: {pool.last_prices() / 1e18}")
    print(f"{token0.symbol()} balance: {pool.balances(0) / 10**token0.decimals()}")
    print(f"{token1.symbol()} balance: {pool.balances(1) / 10**token1.decimals()}")
    print("-" * 80)

    print(f"Total fee: {web3.fromWei(AMOUNT - token0.balanceOf(trader), 'ether')} {token0.symbol()}")

    chain.sleep(60 * SLEEP_MINS)
    chain.mine()
    print("-" * 80)
    print(f"After {SLEEP_MINS}mins...")
    print(f"Price oracle: {pool.price_oracle() / 1e18}")
    print("-" * 80)
