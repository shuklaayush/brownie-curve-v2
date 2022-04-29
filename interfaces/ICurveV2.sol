// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.13;

interface ICurveV2 {
    function last_prices() view external returns (uint256);
    function price_oracle() view external returns (uint256);
    function balances(uint256 arg0) view external returns (uint256);
    function exchange(uint256 i, uint256 j, uint256 dx, uint256 min_dy) payable external returns (uint256);
}
