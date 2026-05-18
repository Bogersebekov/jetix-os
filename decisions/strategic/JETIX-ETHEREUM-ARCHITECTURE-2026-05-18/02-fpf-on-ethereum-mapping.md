---
title: "02 — FPF primitives → Ethereum smart contracts mapping"
date: 2026-05-18
type: fpf-substrate-mapping
F: F3
G: jetix-fpf-on-ethereum-mapping
R: refuted_if_FPF_primitive_misencoded_OR_smart_contract_pattern_inapplicable
constitutional_posture: R1 surface + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
---

# 02 — FPF primitives → Ethereum smart contracts mapping

## §FPF primitives

Core mapping: FPF abstract primitives → concrete Ethereum implementation patterns. Preserves IP-1 (Foundation = abstract role-types; Ethereum addresses = RUSLAN-LAYER overlay bindings).

## §1 Primitive → Implementation matrix

| FPF primitive | Ethereum implementation | Standard / pattern | F-G-R |
|---|---|---|---|
| `U.Role` (A.2) — role-type | Solidity `interface IRole` + role-type registry | ERC-721 (NFT) or custom registry | F3 |
| `U.RoleAssignment` (A.2.1) — Holder#Role:Context binding | Soulbound Token (SBT) — non-transferable ERC-5114 / ERC-4973 / EIP-5114 | EIP-5114 (Soul-bound tokens proposal) | F3 |
| `U.Commitment` (A.2.8) — open commitment | Smart-contract escrow + verifiable conditions | OpenZeppelin Escrow / custom Solidity | F4 |
| `U.SpeechAct` (A.2.9) — signaling | On-chain attestation (event log) | EAS (Ethereum Attestation Service) | F4 |
| `U.PromiseContent` (A.2.3) — promise content | Smart-contract terms (immutable bytecode + parameters) | Solidity contract storage | F4 |
| `U.System` (A.1) — system holon | Diamond Proxy pattern (modular smart-contract clusters) | EIP-2535 Diamond Standard | F3 |
| `A.1.1 U.BoundedContext` — context boundary | Namespace via contract address scope | Foundry / Hardhat deployment scope | F3 |
| `A.3.1 U.Method` — operational method | Function selector + execution logic | Solidity function | F4 |
| `A.3.2 U.MethodDescription` — recipe | Off-chain JSON-LD + on-chain pointer (IPFS hash) | EIP-2477 (Document hash) + IPFS | F3 |
| `A.5 Kernel Modularity` — composable units | Diamond facets + library imports | EIP-2535 + Solidity libraries | F4 |
| `A.6.1 U.Mechanism` — execution substrate | Ethereum L2 rollup itself | OP Stack / Arbitrum Nitro / Base / zkSync | F4 |
| `A.6.B Boundary Norm Square` — boundary discipline | Role-based access control (RBAC) | OpenZeppelin AccessControl | F4 |
| `A.6.C Contract Unpacking` — contract structure | Solidity struct + getter functions | Solidity | F4 |
| `A.7 Strict Distinction` — type discipline | Solidity strict typing (uint256 / address / bytes32) | Solidity | F5 |
| `A.10 Evidence Graph` — evidence trail | Event log + transaction history | Ethereum event indexing (The Graph) | F4 |
| `A.13 Agential Role` — autonomous role | Account Abstraction (ERC-4337) — programmable wallets | ERC-4337 | F4 |
| `A.15.1 U.Work` — work record | Workshop event log + IPFS artefact | Custom Solidity event + IPFS | F3 |
| `A.15.2 U.WorkPlan` — work plan | DAO proposal + execution payload | Aragon OSx / Compound Governor | F4 |
| `A.16 U.Episteme` — shared ontology | On-chain reference registry + IPFS schema | EIP-712 typed data | F3 |
| `B.1.6 Γ_work` — capability composition | Multi-contract composition (Diamond facets + cross-contract calls) | EIP-2535 + interface composition | F3 |
| `B.2 MHT` — meta-holon transition | DAO factory deploying sub-DAOs (sub-Clan emergence) | Aragon OSx + factory pattern | F3 |
| `B.3 F-G-R` — formality/group/reliability | EAS attestation with F-G-R schema | EAS (Ethereum Attestation Service) + custom schema | F3 |
| `B.4 Canonical Evolution Loop` — evolution cycle | DAO governance + smart-contract upgradeability (Diamond proxy) | EIP-2535 + Aragon OSx | F4 |
| `B.5.1 Explore→Operate` — sequencing | Multi-phase DAO governance + stage gates | Custom Solidity stage-gate logic | F3 |
| `E.5 Guard-Rails` — guardrails | Smart-contract require statements + circuit breakers | OpenZeppelin Pausable + custom guards | F4 |
| `E.9 DRR` — decision rationale record | On-chain proposal description + IPFS rationale | DAO proposal text + IPFS | F4 |
| `E.17 MVPK` — multi-view package | NFT metadata with multiple format renderings | ERC-721 metadata + IPFS | F3 |

## §2 Pattern composition examples

### §2.1 Workshop graduation = role-attestation SBT issuance

**FPF composition:**
- `U.RoleAssignment` (A.2.1) attesting Workshop-graduate role
- `U.Commitment` (A.2.8) from issuer (Workshop)
- `B.3 F-G-R` provenance trace (formality F4 + group=workshop + reliability=verified)
- `A.10 Evidence Graph` (Workshop curriculum completion + peer-review)

**Ethereum implementation:**
```solidity
// Pseudocode (simplified)
contract WorkshopGraduationSBT is ERC5114 {
    struct Attestation {
        address graduate;       // U.RoleAssignment holder
        bytes32 roleType;       // U.Role identifier
        uint256 issuedAt;       // A.10 Evidence timestamp
        bytes32 fgrTriple;      // F-G-R hash
        string ipfsMetadata;    // U.MethodDescription pointer
    }
    mapping(uint256 => Attestation) public attestations;
    
    function attest(address graduate, bytes32 roleType, bytes32 fgrTriple, string memory ipfsMetadata) 
        external onlyRole(WORKSHOP_ROLE) {
        // ... mint non-transferable token bound to graduate's soul-address
    }
}
```

**R12 alignment:** non-transferable → no extraction via SBT sale; fork-and-leave preserved via graduate's wallet portability.

### §2.2 Multi-Clan governance vote

**FPF composition:**
- `B.2 MHT` (Clan holons aggregating to multi-Clan holon)
- `A.15.2 U.WorkPlan` (proposed coordinated action)
- `B.4 Canonical Evolution Loop` (vote → execute → evaluate cycle)
- `E.9 DRR` (decision rationale on-chain)

**Ethereum implementation:**
- Aragon OSx DAO per Clan
- Multi-Clan «super-DAO» as Aragon DAO of DAOs (each Clan = one delegate)
- Quadratic Voting via per-Clan delegate weight × QV mechanism
- IPFS for `U.WorkPlan` description + `E.9 DRR` rationale

### §2.3 R12 programmable enforcement

**FPF composition:**
- Pillar C Tier 2 R12 (anti-extraction) — substrate-agnostic foundation_generic
- `E.5 Guard-Rails` — programmable enforcement
- `U.Commitment` (A.2.8) — Clan revenue-sharing commitment

**Ethereum implementation:**
- Revenue-distribution smart contract enforcing 5:1 ratio cap (Mondragón pattern)
- Quadratic Funding contract distributing Workshop revenue (Tang+Weyl pattern)
- Fork-and-leave smart contract allowing member exit with proportional treasury share

**Detail:** `03-r12-programmable-enforcement.md`.

## §3 Off-chain integrations

Not everything goes on-chain. Critical off-chain pieces:

| Component | Off-chain substrate | Why off-chain |
|---|---|---|
| FPF spec docs | Git + Markdown (wiki/) | Authoring-friendly + version-controlled |
| Pattern Language artefact | GitHub + IPFS mirror | Open-source authoring per Plurality precedent |
| Foundation Architecture docs | Git + Markdown (decisions/) | Versioned source-of-truth; hash-anchored on-chain (EIP-2477) |
| Workshop session recordings | Off-chain storage + IPFS optional pointer | Privacy + cost |
| Voice memos / dictations | Off-chain server | Privacy + transcript-derivative on-chain only |
| Sensitive personal data | Off-chain (R12 + GDPR alignment) | Privacy + right-to-be-forgotten |
| PGP signatures (Phase 1) | Off-chain GPG | Substrate diversity preserved |
| Karpathy-wiki-signatures (Phase 1) | Git commit history | Substrate diversity preserved |
| W3C VC v2.0 credentials (Phase 2) | JSON-LD off-chain (default) | Substrate spec flexibility |

**Critical principle:** Ethereum substrate = **complement, not replacement** для off-chain substrates. Layered approach per direction 07 §3.

## §4 Plain English

**Что значит «FPF на Ethereum»?**

Это значит что у нас есть:
- **FPF документы** (Markdown / Git) — описывают **как должна выглядеть система**
- **Ethereum smart contracts** — это **технические реализации** того что описано в FPF

Аналогия: FPF = architectural blueprint дома; Ethereum smart contracts = реальные строительные конструкции. Blueprint описывает «здесь должна быть несущая стена 30см с арматурой»; smart contract = реальная стена в реальном доме.

**Конкретные mappings:**
- «Роль» (FPF) = SBT (Ethereum non-transferable token подтверждающий что ты — Workshop graduate)
- «Голосование Clan» (FPF) = DAO vote через Aragon
- «Распределение revenue» (FPF R12) = revenue distribution smart contract с Mondragón 5:1 ratio cap
- «Fork-and-leave» (FPF R12) = твой кошелёк mobile; ты держишь свои SBTs независимо от Clan governance

**Что НЕ идёт on-chain:**
- Voice memos / personal data — off-chain (privacy)
- FPF spec documents — Git/Markdown (authoring-friendly)
- Workshop session recordings — off-chain (cost + privacy)

**Что на-chain:**
- Role attestations (SBT)
- DAO governance votes
- Revenue distribution (R12 programmable)
- Critical commitments (smart-contract escrow)

## §5 Mermaid: FPF → Ethereum pattern flow

**Detail:** `diagrams/01-jetix-ethereum-stack.md`.

## §6 Open questions

| OQ | Question |
|---|---|
| **OQ-02-1** | EAS (Ethereum Attestation Service) vs custom SBT registry — which? |
| **OQ-02-2** | EIP-5114 vs ERC-5484 vs custom for SBT — pick standard or wait for ratification? |
| **OQ-02-3** | Diamond Proxy (EIP-2535) — upgradeability vs immutability trade-off (R12 angle: upgradeability = potential extraction vector if owner = central party) |
| **OQ-02-4** | The Graph (subgraph indexer) for Evidence Graph — production-ready? |

## §7 Counter-positions

- **Counter 1 (eng critic):** «Smart contracts are buggy. SBT spec not finalized (EIP-5114 draft).» Mitigation: Phase 2+ deployment after spec ratification + extensive audit + start with simple contracts; complexity grows incrementally.
- **Counter 2 (phil critic):** «Mapping FPF → Solidity may distort FPF semantics. FPF is methodology-level; Solidity is execution-level. Translation loss possible.» Mitigation: FPF spec remains canonical Markdown/Git source-of-truth; Ethereum = derivative; translation validated through DOGFOOD use.
- **Counter 3 (sys integrator):** «Diamond Proxy upgradeability = R12 attack surface. Owner could mutate revenue contract to extract.» Mitigation: Diamond Proxy used only for non-financial contracts; revenue contracts = immutable + DAO-governed upgrades only.

## §8 Sources

- EIP-2535 Diamond Standard: eips.ethereum.org/EIPS/eip-2535
- EIP-5114 Soulbound Badges: eips.ethereum.org/EIPS/eip-5114
- EIP-4337 Account Abstraction: eips.ethereum.org/EIPS/eip-4337
- Ethereum Attestation Service: attest.org
- The Graph: thegraph.com
- OpenZeppelin Contracts: docs.openzeppelin.com/contracts
- Aragon OSx: aragon.org

**Word count:** ~1380.
