using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System.Numerics;

namespace RandomNumbers
{
    public class Contract : SmartContract
    {
        public static void Main()
        {
            long numberOfTickets = 666;
            Header header = Blockchain.GetHeader(Blockchain.GetHeight());
            long randomNumber = (long)(header.ConsensusData >> 32);
            long winningTicket = (randomNumber * numberOfTickets) >> 32;
            Runtime.Notify("The winning ticket is:", winningTicket);
        }
    }
}