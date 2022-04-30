#!/usr/bin/env python3
from brownie import accounts, chain, interface, web3, Contract, Trader

POOL = "0xF43b15Ab692fDe1F9c24a9FCE700AdCC809D5391"

AMOUNT = web3.toWei(10_000, "ether")
SLEEP_MINS = 30


def main():
    accounts.default = accounts[0]

    trader = Trader.deploy(POOL)

    pool = interface.ICurveV2(POOL)
    token0 = interface.IERC20(trader.token0())
    token1 = interface.IERC20(trader.token1())

    interface.IWeth(token0).deposit({"value": AMOUNT})
    token0.transfer(trader, AMOUNT)

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
