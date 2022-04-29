// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.13;

interface IERC20 {
    function decimals() view external returns (uint8);
    function approve(address _spender, uint256 _amount) external returns (bool success);
    function balanceOf(address _owner) view external returns (uint256 balance);
    function transfer(address _to, uint256 _amount) external returns (bool success);
}


